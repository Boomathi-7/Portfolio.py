import streamlit as st

def main():
    st.set_page_config(page_title="My Portfolio", page_icon="💼", layout="centered")

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to:", ["Home", "About Me", "Projects", "Contact"])

    if page == "Home":
        st.title("💼 Welcome to My Portfolio!")
        st.write(
            """
            Hello! I'm BOOMATHI P, a college student with a passion for software development. 
            Explore my resume, projects, and more using the navigation on the left.
            """
        )
        st.write("🌟 Let's build something amazing together!")

    elif page == "About Me":
        st.title("🙋‍♂️ About Me")
        st.write(
            """
            **Name:** BOOMATHI P\n
            **Role:** Student \n
            **Location:** Coimbatore, India 
            """
        )
        st.subheader("Skills")
        st.write(
            """
            - **Programming Languages:** Python
            - **Web Development:** HTML
            - **Other Skills:** Problem-Solving, Communication, Aptitude
            """
        )

    elif page == "Projects":
        st.title("💻 Projects")
        st.write(
            """
            Here are some of the projects I've worked on:
            """
        )
        st.subheader("Project 1: CodSoft")
        st.write(
            """
            Description: An internship at CodSoft, where I completed several tasks like Calculator App, To-Do List, Rock-Paper-Scissors Game, Contact Book and Password Generator.
            Technologies: Python
            [GitHub Repo](https://github.com/Boomathi-7/CodSoft.git) 
            """
        )
        st.subheader("Project 2: Guessing Game")
        st.write(
            """
            Description: Number Guessing Game has been done. Here the code prompts the user to guess the number which it randomly chooses. 
            Technologies: Python, Streamlit  
            [GitHub Repo](https://github.com/Boomathi-7/guessinggame.py.git) 
            """
        )

    elif page == "Contact":
        st.title("📬 Contact Me")
        st.write("Feel free to reach out!")
        contact_form = """
        <form action="https://formsubmit.co/YOUR_EMAIL" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your Name" required>
            <input type="email" name="email" placeholder="Your Email" required>
            <textarea name="message" placeholder="Your Message" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
