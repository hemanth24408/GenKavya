
import streamlit as st
from generator import generate_verses
import base64
from pathlib import Path

st.set_page_config(
    page_title="GenKavya | Sanskrit Padyam",
    page_icon="📜",
    layout="centered"
)

# Load the background image
image_path = Path(__file__).parent / "background.png"

if not image_path.exists():
    st.error(f"Background image not found: {image_path}")
else:
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(
            image_file.read()
        ).decode("utf-8")

    st.markdown(
        f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url(
                "data:image/png;base64,{encoded_image}"
            );
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        [data-testid="stMain"] {{
            background-color: transparent;
        }}

        [data-testid="stHeader"] {{
            background-color: transparent;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    
# Traditional Sanskrit-inspired styling
st.markdown("""
<style>
.stApp {
    color: #3B2025;
}

.block-container {
    max-width: 850px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1, h2, h3 {
    color: #702632 !important;
    font-family: Georgia, serif;
}

p, label, .stMarkdown {
    color: #3B2025;
}

.subtitle {
    color: #785B50;
    font-size: 1.05rem;
    text-align: center;
}

.ornament {
    color: #A47B37;
    text-align: center;
    font-size: 1.4rem;
    margin: 0.5rem 0 1rem 0;
}

.section-label {
    color: #702632;
    font-weight: 600;
    font-size: 1.1rem;
    margin-top: 1rem;
}

div.stButton > button {
    background-color: #702632;
    color: #FFF9F0;
    border: 1px solid #702632;
    border-radius: 8px;
    padding: 0.6rem 1.5rem;
    font-weight: 600;
    width: 100%;
}

div.stButton > button:hover {
    background-color: #541B25;
    color: white;
    border-color: #541B25;
}

div[data-testid="stTextArea"] textarea {
    background-color: #FFFCF6;
    color: #3B2025;
    border: 1px solid #CBB99D;
    border-radius: 8px;
}

div[data-testid="stTextArea"] textarea:focus {
    border-color: #702632;
    box-shadow: 0 0 0 1px #702632;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #FFFCF6;
    border-color: #D9C8AD;
    border-radius: 12px;
}



.footer {
    text-align: center;
    color: #8B7564;
    font-size: 0.85rem;
    margin-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown(
    '<div class="ornament">॥ श्रीः ॥</div>',
    unsafe_allow_html=True
)

st.title("GenKavya")
st.markdown(
    '<p class="subtitle">'
    'From your story to Sanskrit poetry'
    '</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="ornament">❖ ───── ❖ ───── ❖</div>',
    unsafe_allow_html=True
)

st.write(
    "Enter a story in English and transform it into "
    "a Sanskrit padyam in Anuṣṭubh metre."
)

st.markdown(
    '<p class="section-label">Your Story</p>',
    unsafe_allow_html=True
)

story = st.text_area(
    "Enter your story in English",
    placeholder=(
        "For example: A boy saw a thirsty bird, "
        "gave it water, and the bird became happy."
    ),
    height=180,
    max_chars=500,
    label_visibility="collapsed"
)

st.caption(
    f"{len(story)} / 500 characters"
)

generate_button = st.button(
    "✦  Generate Padyam  ✦",
    type="primary"
)

if generate_button:
    if not story.strip():
        st.warning("Please enter a story first.")
    else:
        with st.spinner(
            "Composing Sanskrit poetry... कृपया प्रतीक्षताम्"
        ):
            try:
                result = generate_verses(
                    story,
                    number_of_candidates=5
                )

                summary = result.get("story_summary")
                if summary:
                    st.markdown("### Story Summary")
                    st.write(summary)

                candidates = result.get("candidates", [])

                if candidates:
                    st.markdown(
                        '<div class="ornament">'
                        '॥ सुभाषितम् ॥'
                        '</div>',
                        unsafe_allow_html=True
                    )

                    for index, candidate in enumerate(candidates, start=1):
                        with st.container(border=True):
                            st.markdown(
                            f"<h3 style='text-align:center;'>"
                             f"॥ Padyam {index} ॥</h3>",
                             unsafe_allow_html=True
                        )

                        st.markdown(
                        '<div style="text-align:center;'
                        'font-size:1.3rem;'
                        'line-height:2.2;'
                        'padding:1rem 0;">'
                        + "<br>".join(candidate["padas"])
                        + "</div>",
                        unsafe_allow_html=True
                        )

                        st.divider()

                        st.markdown("**Meaning**")
                        st.write(
                        candidate.get(
                            "meaning",
                            "Meaning not provided."
                            )
                        )   

                        st.caption("Metre: Anuṣṭubh (अनुष्टुभ्)")
                else:
                    st.warning(
                        result.get(
                            "message",
                            "No padyams passed metre validation. "
                            "Please try again."
                        )
                    )

            except Exception as error:
                st.error(
                    f"Unable to generate the padyam: {error}"
                )

st.markdown(
    '<div class="footer">'
    'GenKavya · संस्कृतकाव्यनिर्माणम्'
    '</div>',
    unsafe_allow_html=True
)
