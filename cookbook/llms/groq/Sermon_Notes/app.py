import streamlit as st
from phi.tools.youtube_toolkit import YouTubeTools
from assistant import get_chunk_summarizer, get_video_summarizer  # type: ignore

st.set_page_config(
    page_title="Connect Group Facilitator's Notes Creator",
    page_icon=":pray:",
)
st.title("Connect Group Facilitator's Notes Creator")
st.markdown("##### :pray: built using [phidata](https://github.com/phidatahq/phidata)")


def main() -> None:
    # Get model
    llm_model = st.sidebar.selectbox(
        "Select Model", options=["llama3-70b-8192", "llama3-8b-8192", "mixtral-8x7b-32768"]
    )
    # Set assistant_type in session state
    if "llm_model" not in st.session_state:
        st.session_state["llm_model"] = llm_model
    # Restart the assistant if assistant_type has changed
    elif st.session_state["llm_model"] != llm_model:
        st.session_state["llm_model"] = llm_model
        st.rerun()

    # Get chunker limit
    chunker_limit = st.sidebar.slider(
        ":pencil: Words in chunk",
        min_value=1000,
        max_value=10000,
        value=2000,
        step=500,
        help="Set the number of characters to chunk the text into.",
    )

    # Sidebar selection for input type
    input_type = st.sidebar.radio("Select Input Type", options=["Video URL", "Text"])

    if input_type == "Video URL":
        # Get video url
        video_url = st.sidebar.text_input(":video_camera: Sermon Video URL")

        # Button to generate notes
        generate_notes = st.sidebar.button("Generate Facilitator Notes")
        if generate_notes:
            st.session_state["youtube_url"] = video_url

    elif input_type == "Text":
        # Get text input
        text_input = st.sidebar.text_area(":pencil2: Sermon Transcript", height=200)

        # Button to generate notes
        generate_notes = st.sidebar.button("Generate Facilitator Notes")
        if generate_notes:
            st.session_state["text_input"] = text_input

    st.sidebar.markdown("## Trending Sermons")
    if st.sidebar.button("Sermon 1"):
        st.session_state["youtube_url"] = "https://youtu.be/sermon_link_1"
    if st.sidebar.button("Sermon 2"):
        st.session_state["youtube_url"] = "https://youtu.be/sermon_link_2"
    if st.sidebar.button("Sermon 3"):
        st.session_state["youtube_url"] = "https://youtu.be/sermon_link_3"

    if input_type == "Video URL" and "youtube_url" in st.session_state:
        _url = st.session_state["youtube_url"]
        youtube_tools = YouTubeTools(languages=["en"])
        video_captions = None
        video_summarizer = get_video_summarizer(model=llm_model)
        with st.status("Parsing Sermon Video", expanded=False) as status:
            with st.container():
                video_container = st.empty()
                video_container.video(_url)
            video_data = youtube_tools.get_youtube_video_data(_url)
            with st.container():
                video_data_container = st.empty()
                video_data_container.json(video_data)
            status.update(label="Video", state="complete", expanded=False)
        with st.status("Reading Captions", expanded=False) as status:
            video_captions = youtube_tools.get_youtube_video_captions(_url)
            with st.container():
                video_captions_container = st.empty()
                video_captions_container.write(video_captions)
            status.update(label="Captions processed", state="complete", expanded=False)
        if not video_captions:
            st.write("Sorry, could not parse the sermon video. Please try again or use a different video.")
            return

        chunks = []
        num_chunks = 0
        words = video_captions.split()
        for i in range(0, len(words), chunker_limit):
            num_chunks += 1
            chunks.append(" ".join(words[i : (i + chunker_limit)]))
        if num_chunks > 1:
            chunk_summaries = []
            for i in range(num_chunks):
                with st.status(f"Summarizing chunk: {i+1}", expanded=False) as status:
                    chunk_summary = ""
                    chunk_container = st.empty()
                    chunk_summarizer = get_chunk_summarizer(model=llm_model)
                    chunk_info = f"Sermon Video Data: {video_data}\n\n"
                    chunk_info += f"{chunks[i]}\n\n"
                    for delta in chunk_summarizer.run(chunk_info):
                        chunk_summary += delta  # type: ignore
                        chunk_container.markdown(chunk_summary)
                    chunk_summaries.append(chunk_summary)
                    status.update(label=f"Chunk {i+1} summarized", state="complete", expanded=False)
            with st.spinner("Generating Facilitator Notes"):
                summary = ""
                summary_container = st.empty()
                video_info = f"Sermon Video URL: {_url}\n\n"
                video_info += f"Sermon Video Data: {video_data}\n\n"
                video_info += "Summaries:\n\n"
                for i, chunk_summary in enumerate(chunk_summaries, start=1):
                    video_info += f"Chunk {i}:\n\n{chunk_summary}\n\n"
                    video_info += "---\n\n"
                for delta in video_summarizer.run(video_info):
                    summary += delta  # type: ignore
                    summary_container.markdown(summary)
        else:
            with st.spinner("Generating Facilitator Notes"):
                summary = ""
                summary_container = st.empty()
                video_info = f"Sermon Video URL: {_url}\n\n"
                video_info += f"Sermon Video Data: {video_data}\n\n"
                video_info += f"Captions: {video_captions}\n\n"
                for delta in video_summarizer.run(video_info):
                    summary += delta  # type: ignore
                    summary_container.markdown(summary)

    elif input_type == "Text" and "text_input" in st.session_state: 
        text_input = st.session_state["text_input"]
        # ... (logic for processing text input using get_chunk_summarizer()) ...

    else:
        st.write("Please provide input or click on one of the trending sermons.")

    st.sidebar.markdown("---")
    if st.sidebar.button("Restart"):
        st.rerun()


main()