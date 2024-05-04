#This code was generated from Gemini 1.5 pro latest
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
        description="You are a Junior Connect Group Facilitator tasked with generating summary notes for a sermon.",
        instructions=[
            "You will be provided with a sermon transcript.",
            "Carefully read the transcript and compile a succinct summary of the content.",
            "Include all scripture references"
            "Exclude any announcements, altar calls or receiving of communion at the start or end of the transcript"
        ],
        add_to_system_prompt=dedent("""
        <notes_format>
        ### Key Verses
        {List all the Bible verses referenced in the sermon. Do not duplicate verses. Exclude verses where the full reference(book, chapter and verse) is not given}
        **{Exclude verses where the full reference are not given}
        **{Exclude implied or inferred scripture references}    
        ### Sermon Overview
        {Provide a summary of the central theme and key points of the sermon.}
        {Identify the main themes and briefly elaborate on each.}
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
        description="You are a Senior Connect Group Facilitator tasked with generating connect group facilitator discussion notes for a sermon video / audio.",
        instructions=[
            "You will be provided with:"
            "  1. Sermon video link and information about the sermon"
            "  2. Pre-processed summaries from junior researchers."
            "Carefully process the information and think about the contents.",
            "Then generate comprehensive connect group notes in the <notes_format> provided below.",
            "Discuss each of the main themes identified and make the notes engaging, informative, and well-structured.",
            "Ensure the title is a markdown link to the video.",
            "Break the notes into sections and include closing remarks.",
            "Make sure the notes are properly formatted."
            "The notes will be used during connect- /small-group discussions during the weekly meetups following the Sunday that the sermon was preached"
            "The purpose is the discuss the key themes, princples and lessons in a group setting, with an emphasis on maximum group praticipation in discussions and to reinforce the message of the sermon"
            "Each theme / princple / lesson will be discussed by asking someone to read the relevant scripture verse/verses which is following by a question(s). After answers and group discussion, a model answer is read and discussed"
        ],
        add_to_system_prompt=dedent("""
        <notes_format>
        ## Sermon Title: {sermon_title} by {speaker_name}

        ### Key Verses
        {List all the Bible verses referenced in the sermon. Exclude verses where the full reference are not given. Exclude verses where the full reference are not given. Exclude implied of inferred verses}
        **{Exclude verses where the full reference are not given}
        **{Exclude implied of inferred verses}   
        ### Sermon Overview
        {Provide a concise summary of the central theme and key points of the sermon.}
        **{Write from the persepctive of a serving member (e.g. connect group leader) in the church, i.e. do refer to the pastor as "the speaker", rather say e.g. "Pastor Josh" or "Pastor Kabelo" or "PAstor Wayne" or "Pastor Tara" using the first name etc. using the name of the pastor conductiong the sermon }
        {Identify the main themes and briefly elaborate on each.}
        ### Discussion Questions
        {Develop thought-provoking questions for each theme to encourage group interaction, reflection, and application.}
        {Include practical examples when discussing each theme.}
        **{Always try to start each question with the reading of a relevant scripture verse (according to the sermon) that illustrates the theme/principle/lesson. Include the text of the verse as well. Do not use the same scripture in more than one theme. The question posed is then about how the e.g., principle/lesson in the verse about God's power, promises, love, or faithfulness and His love, care, protection, provision for us or the power of faith and trust in God or Jesus Christ illustrates the theme/lesson/principle.}** 
        **{Include the text of the scripture verse after the scripture reference at the start of the question}
        **{questions should be listed after the respective theme heading }
        **{After each question provide an answer to the question, demonstrating how the principle in the scripture verse answers the question. Use the relevant sections of the sermon to support the answer. Use a practical example if neccessary, to help with the practical application of the verse. The facilitator will discuss this answer after the group discussion of each question}                            
          {Continue with the development of questions for the remainder of the themes using the format above.}
                                                                 
        ### Activities (Optional)
        {Suggest 1-2 engaging activities related to the themes, such as e.g. group discussions.}
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
