import streamlit as st
import streamlit.components.v1 as components
import base64
import time
from typing import List, Dict

# Set the page configuration
st.set_page_config(page_title="My Streamlit App", page_icon="💕")

# Add pulsing effect to title
st.markdown(
    """
    <style>
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.5; }
        100% { opacity: 1; }
    }
    .pulsing {
        animation: pulse 4s infinite;
        font-size: 2rem;
        font-weight: bold;
        color: white;
        text-align: center;
    }
    </style>
    <div class="pulsing">Our love is an endless journey ...</div>
    """,
    unsafe_allow_html=True,
)
# Theme colors
theme_colors: List[str] = ["#6f676f", "#ca8d90", "#f7c2cf", "#a96177", "#0e5b6a"]


def load_audio(file_path: str) -> bytes:
    """
    Load the audio file and return its bytes.

    Args:
    file_path (str): The path to the audio file.

    Returns:
    bytes: The audio file's content in bytes.
    """
    with open(file_path, "rb") as audio_file:
        audio_bytes = audio_file.read()
    return audio_bytes


def get_audio_base64(audio_bytes: bytes) -> str:
    """
    Encode the audio bytes to a base64 string.

    Args:
    audio_bytes (bytes): The audio file's content in bytes.

    Returns:
    str: The audio file's content encoded in base64.
    """
    return base64.b64encode(audio_bytes).decode()


def audio_html(audio_base64: str) -> str:
    """
    Generate the HTML for a hidden audio player.

    Args:
    audio_base64 (str): The audio file's content encoded in base64.

    Returns:
    str: HTML string for the hidden audio player.
    """
    return f"""
    <audio autoplay loop style="display:none;">
        <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
        Your browser does not support the audio element.
    </audio>
    """


# Define the theme using extracted colors
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {theme_colors[2]};
        color: {theme_colors[0]};
    }}
    .stButton button {{
        background-color: {theme_colors[1]};
        color: white;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Poems
poem1: str = """The first true photo<br>
Neither of us sure if it would be the last<br>
But nudging elbows, smirking eyes, and our racing hearts<br>
Insisted that this was just the start<br>"""


poem2: str = """A chance encounter<br>
A painful chapter for you<br>
A busy one for me<br>
But my heart insisted then<br>
As it still insists now <br>
Your pain is mine, and you’ll never face it alone"""


poem3: str = """Joy poured down… <br>
Harder than the rain<br>
Louder than the fear and doubt<br>
Brighter than our hopes and dreams<br>
Our hearts were finally free to hold each other"""

poem4: str = """A leap of faith often starts with a step of trust<br>
Me leading you into the unknown, the seemingly undesirable, but the unenjoyed<br>
I have loved watching the person I coaxed out to the bar<br> 
Blossom into the woman leads me into and embrace adventure after adventure<br>
Your openness and your willingness to try the new brings so much spice and flavor to our lives"""


poem5: str = """The first of the black man - white woman makeup flops<br>
(certainly not the last) <br>
A night were a couple’s candle went out, ours grew brighter<br>
From then, I knew there was a whole world people we could help<br>
The past said foster children and the future whispers troubled youth<br>
I know we have a lot to offer, a lot to build, and lot to nurture"""


poem6: str = """One of many celebrations<br>
I’m in love with a love that celebrates itself<br>
I’m in love with a women who makes her people feel special<br>
I can’t wait to show her that though she doesn’t give to receive,<br>
There will always be at least one person who dare to give as much as she she can receive"""

poem7: str = """A perfect day, if there were any<br>
A walk to the park <br>
A newfound love of pillars<br>
A fantastic meal <br>
A harmless (or potentially traumatic) prank on the young one (simon)<br>
And lots of yapping in between<br><br> 
But when disasters strikes:<br>
One lost phone, a set of missing keys, medicine left at the airport, an unscratched back, or even a forehead unkissed <br><br>
There are no depths I wouldn’t plunge, no lengths I wouldn’t go, and no hell I wouldn’t dive into for you"""


poem9: str = """I choose the uncertainty of love<br><br> 
The long walk on the beach <br>
The full belly <br>
The sandy feet <br>
The shared smiles<br>
The locked arms <br>
And the unexpected surprises along the way"""


poem10: str = """I choose the spontaneity of love<br><br>
The raging concerts<br>
The “1st-day-met best friends”<br>
The sprints in the rain<br> 
The spills (not my fault) in the parking lots<br>
The late night food<br> 
The … 👀"""

poem11: str = """I choose the longing of love<br><br>
The moments we can't get close enough<br> 
We can't moments we can't bare to be apart<br> 
The moments where no words can describe the restless, intoxicating, magnetic pleasure that draws us together<br>
Though that’s not what holds us together<br>
It’s a pleasant reward for daring to love and allowing oneself to be loved"""


poem12: str = """I choose the vision of love<br><br>
The “let's build”<br>
The “let's grow”<br>
The “let's heal”<br>
The “I’m right by your side”<br>
The “I know we got this”<br> 
The “Nothing (but spontaneous farting) can stop us”"""


poem13: str = """I choose laugher of love<br><br>
Endless, unescapable, unprovoked laughter<br>
Laughing at:<br> 
- The many tv shows we start and don’t finish <br>
- Simon and his peculiar sitting habits<br>
- Each other 
- Each other but not in a good way (jk.. Or Am I?)
We will celebrate the day our first wrinkles will come in <br>
And I will be the first to apologize for being too funny for your face to keep up<br> 
(and I’m sure you’ll have plenty to say about that)"""


poem14: str = """I choose loving with actions<br><br>
Home cooked meals<br>
Weeded yards<br>
Collaborated on resumes<br>
Scratched backs<br>
Planned dates<br> 
I know we’ll be in a lifelong competition to out serve each other, and I don’t plan to lose<br>
(game on ;) )"""


poem15: str = """I choose independent play<br><br>
Pursuing our hobbies while enjoying each others company<br>
I’m so happy that 🥳<br>
my gamer girlfriend 🎉<br>
became my gamer wife 🪩<br>
and supports our (my) gaming life 🎊<br>"""


poem16: str = """I choose the the long-haired beauty<br><br> 
Who’s back can never be scratched enough<br>
Who single handedly drives the coca-cola and dr pepper sales in west michigan<br> 
Who’s eyes are equally captivating and welcoming<br> 
Who has a witty comeback for everything<br> 
Who loves and cares for her people so dearly <br> 
Who has the most pampered dog in north America<br> 
Who cooks like her love is one of the ingredients<br> 
Who could (and probably has) sleep 24 hours straight if left unattended <br> 
Who gives herself so wholeheartedly to everything she is involved in<br>  
Who will make and makes  a great mother, foster mother, aunt, sister, neighbor, mentor, sister, daughter, and friend<br>  
Who’s ego will get too big if I go any longer<br><br> 
I choose you and everything that comes with you<br>
I love you, cherish and appreciate you<br><br>   
Happy 4 months, Mrs. Mwesigwa"""


# Display series of pictures and poems
images_and_poems: List[Dict[str, str]] = [
    {"image": "photos/Image1.JPG", "poem": poem1},
    {"image": "photos/Image2.JPG", "poem": poem2},
    {"image": "photos/Image3.JPG", "poem": poem3},
    {"image": "photos/Image4.jpg", "poem": poem4},
    {"image": "photos/image5.JPEG", "poem": poem5},
    {"image": "photos/Image6.JPG", "poem": poem6},
    {"image": "photos/Image7.jpg", "poem": poem7},
    {"image": "photos/Image9.jpg", "poem": poem9},
    {"image": "photos/Image10.PNG", "poem": poem10},
    {"image": "photos/Image11.jpg", "poem": poem11},
    {"image": "photos/Image12.jpg", "poem": poem12},
    {"image": "photos/Image13.jpg", "poem": poem13},
    {"image": "photos/Image14.jpg", "poem": poem14},
    {"image": "photos/image15.jpg", "poem": poem15},
    {"image": "photos/Image16.jpg", "poem": poem16},
]


def display_image(image_path: str) -> None:
    """
    Display an image with styling.

    Args:
    image_path (str): Path to the image file.
    """
    st.image(image_path, use_column_width=True, output_format="auto")


def display_poem(poem: str) -> None:
    """
    Display a poem with styling and hover effect.

    Args:
    poem (str): The poem to display.
    """
    st.markdown(
        f"""
        <div class="poem" style="animation: pulse 5s infinite; text-align: center; font-size: 16px; color: white; font-style: italic; line-height: 1.5; transition: transform 0.2s ease-in-out;">
        {poem}
        </div>
        <style>
        .poem:hover {{
            transform: scale(1.05);
        }}
        @media only screen and (max-width: 600px) {{
            .poem {{
                font-size: 14px;
                line-height: 1.4;
            }}
            .pulsing {{
                font-size: 1.5rem;
            }}
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def display_navigation_buttons(current: int, total: int) -> int:
    """
    Display navigation buttons and return the updated index.

    Args:
    current (int): The current index.
    total (int): The total number of items.

    Returns:
    int: The updated index.
    """
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col1:
        if st.button("←", disabled=(current == 0)):
            return current - 1 if current > 0 else current
    
    with col3:
        if st.button("→", disabled=(current == total - 1)):
            return current + 1 if current < total - 1 else current
    
    return current

def display_slideshow(images_and_poems: List[Dict[str, str]], delay: int = 10) -> None:
    """
    Display a slideshow of images and poems with a delay between transitions.

    Args:
    images_and_poems (List[Dict[str, str]]): A list of dictionaries with 'image' and 'poem' keys.
    delay (int): Delay in seconds between transitions. Default is 10 seconds.
    """

    if "index" not in st.session_state:
        st.session_state.index = 0

    st.session_state.index = display_navigation_buttons(st.session_state.index, len(images_and_poems))
    

    display_image(images_and_poems[st.session_state.index]["image"])
    display_poem(images_and_poems[st.session_state.index]["poem"])
    


# Path to your audio file
audio_file_path: str = "music/midnight.mp3"

# Load and encode the audio file
audio_bytes: bytes = load_audio(audio_file_path)
audio_base64: str = get_audio_base64(audio_bytes)

# Render the hidden audio player
components.html(audio_html(audio_base64), height=0, width=0)

# Display the slideshow
display_slideshow(images_and_poems)
