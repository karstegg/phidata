#This code was generated from GPT4
from textwrap import dedent
from phi.llm.groq import Groq
from phi.assistant import Assistant

def get_chunk_summarizer(
    model: str = "llama3-70b-8192",
    debug_mode: bool = True,
) -> Assistant:
    """Get a Groq Research Assistant."""

    return Assistant(
        name="groq_sermon_chunk_summarizer",
        llm=Groq(model=model),
        description="You are a Senior Connect Group Facilitator tasked with generating discussion notes for a sermon.",
        instructions=[
            "You will be provided with a sermon transcript.",
            "Carefully read the transcript and prepare comprehensive connect group notes.",
            "Identify and reinforce 3-5 key themes/points/messages from the sermon through targeted discussion questions and activities.",
            "Ensure the notes follow the <notes_format> provided below."
        ],
        add_to_system_prompt=dedent("""
        <notes_format>
        ### Launch
        {Describe a time when fear held you back from something you wanted to do. How did you feel, and what did you do about it?}

        ### Definition
        {Provide definitions of key concepts or terms from the sermon, including practical applications or examples.}

        ### Key Scripture
        {List the main Bible verses referenced in the sermon.}

        ### Sermon Overview
        {Provide a concise summary of the central theme and key points of the sermon.}
        {Identify the 3-5 main themes/points/messages and briefly elaborate on each.}

        ### Discussion Questions
        {Develop thought-provoking questions for each theme to encourage group interaction, reflection, and application.}
        {Include practical examples or case studies when discussing each theme.}

        ### Theme 1
        {Develop 2-3 questions specifically related to Theme 1.}

        ### Theme 2
        {Develop 2-3 questions specifically related to Theme 2.}

        ### Theme 3
        {Develop 2-3 questions specifically related to Theme 3.}

        ### Activities (Optional)
        {Suggest 1-2 engaging activities related to the themes, such as role-playing or group discussions.}

        ### Closing Remarks
        {Provide a summary or final thoughts to wrap up the discussion.}
        {Incorporate a reflective question or challenge into the closing remarks to encourage personal application.}

        </notes_format>
        """),
        # This setting tells the LLM to format messages in markdown
        markdown=True,
        add_datetime_to_instructions=True,
        debug_mode=debug_mode,
    )


def get_video_summarizer(
    model: str = "llama3-70b-8192",
    debug_mode: bool = True,
) -> Assistant:
    """Get a Groq Research Assistant."""

    return Assistant(
        name="groq_sermon_video_summarizer",
        llm=Groq(model=model),
        description="You are a Senior Connect Group Facilitator tasked with generating discussion notes for a sermon video.",
        instructions=[
            "You will be provided with:"
            "  1. Sermon video link and information about the sermon"
            "  2. Pre-processed summaries from junior researchers."
            "Carefully process the information and think about the contents.",
            "Then generate comprehensive connect group notes in the <notes_format> provided below.",
            "Make the notes engaging, informative, and well-structured.",
            "Ensure the title is a markdown link to the video.",
            "Break the notes into sections and include closing remarks.",
            "Make sure the notes are properly formatted and sensitive to group members' backgrounds."
        ],
        add_to_system_prompt=dedent("""
        <notes_format>
        ## Sermon Video Title with Link
        {this is the markdown link to the video}

        ### Launch
        {Describe a time when fear held you back from something you wanted to do. How did you feel, and what did you do about it?}

        ### Definition
        {Provide definitions of key concepts or terms from the sermon, including practical applications or examples.}

        ### Key Scripture
        {List the main Bible verses referenced in the sermon.}

        ### Sermon Overview
        {Provide a concise summary of the central theme and key points of the sermon.}
        {Identify the 3-5 main themes/points/messages and briefly elaborate on each.}

        ### Discussion Questions
        {Develop thought-provoking questions for each theme to encourage group interaction, reflection, and application.}
        {Include practical examples or case studies when discussing each theme.}

        ### Theme 1
        {Develop 2-3 questions specifically related to Theme 1.}

        ### Theme 2
        {Develop 2-3 questions specifically related to Theme 2.}

        ### Theme 3
        {Develop 2-3 questions specifically related to Theme 3.}

        ### Activities (Optional)
        {Suggest 1-2 engaging activities related to the themes, such as role-playing or group discussions.}

        ### Closing Remarks
        {Provide a summary or final thoughts to wrap up the discussion.}
        {Incorporate a reflective question or challenge into the closing remarks to encourage personal application.}

        Report generated on: {Month Date, Year (hh:mm AM/PM)}
        </notes_format>
        """),
        # This setting tells the LLM to format messages in markdown
        markdown=True,
        add_datetime_to_instructions=True,
        debug_mode=debug_mode,
    )
