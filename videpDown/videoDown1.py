import streamlit as st
import youtube_dl
st.title(" YouTube Downloader")
#Enter the URL
link = st.text_input("Enter the link here")
options = {"format": "bestvideo+bestaudio"}
submit = st.button("download")
def download(link):
    try:
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([link])
        if submit:
            st.success("successfully downloaded")

    except youtube_dl.utils.DownloadError:
        raise st.error('this URL is invalid')


if __name__ == '__main__':
    download("https://www.youtube.com/watch?v=KL8fCSLZfLM")