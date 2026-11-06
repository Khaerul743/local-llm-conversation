import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage

from src.services.chat_service import ChatService

st.set_page_config(
    page_title="Ruang Bicara",
    page_icon=":material/forum:",
    layout="centered",
)

st.markdown(
    """
	<style>
	@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=DM+Serif+Display&display=swap');

	:root {
		--ink: #20342f;
		--muted: #71817a;
		--paper: #f7f8f4;
		--accent: #bd4d35;
		--line: #dce4dc;
	}
	.stApp { background: var(--paper); color: var(--ink); }
	[data-testid="stHeader"] { background: transparent; }
	[data-testid="stSidebar"] { background: #edf2eb; border-right: 1px solid var(--line); }
	html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
	h1, h2, h3 { font-family: 'DM Serif Display', Georgia, serif !important; color: var(--ink); }
	.eyebrow {
		color: var(--accent); font-size: 0.72rem; font-weight: 700;
		letter-spacing: 0.12em; text-transform: uppercase; margin-bottom: 0.3rem;
	}
	.intro { color: var(--muted); font-size: 0.97rem; margin-top: -0.5rem; }
	[data-testid="stChatMessage"] { border: 1px solid var(--line); border-radius: 8px; }
	[data-testid="stChatInput"] { border-color: var(--line); }
	.stButton button { border-radius: 6px; }
	</style>
	""",
    unsafe_allow_html=True,
)

if "chat_service" not in st.session_state:
    try:
        st.session_state.chat_service = ChatService()
        st.session_state.conversation_id = (
            st.session_state.chat_service.create_conversation()
        )
    except Exception as error:
        st.error(f"Gagal menghubungkan ke model bahasa: {error}")
        st.stop()

chat_service: ChatService = st.session_state.chat_service
conversation_id: str = st.session_state.conversation_id

with st.sidebar:
    st.markdown("### :material/forum: Ruang Bicara")
    st.caption("Asisten AI pribadi")
    st.divider()
    if st.button("Percakapan baru", icon=":material/add:", use_container_width=True):
        st.session_state.conversation_id = chat_service.create_conversation()
        st.rerun()
    st.caption("Riwayat percakapan tersimpan selama sesi ini.")

st.markdown('<p class="eyebrow">Asisten AI</p>', unsafe_allow_html=True)
st.title("Apa yang ingin kamu bahas?")
st.markdown(
    '<p class="intro">Tulis pertanyaan atau ide. Jawaban akan muncul secara langsung.</p>',
    unsafe_allow_html=True,
)

history = chat_service.get_history(conversation_id)
for message in history:
    if isinstance(message, HumanMessage):
        role = "user"
    elif isinstance(message, AIMessage):
        role = "assistant"
    else:
        continue
    with st.chat_message(role):
        st.markdown(message.content)

if prompt := st.chat_input("Ketik pesan..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        try:
            st.write_stream(chat_service.stream_message(conversation_id, prompt))
        except Exception as error:
            st.error(f"Pesan tidak dapat diproses: {error}")
