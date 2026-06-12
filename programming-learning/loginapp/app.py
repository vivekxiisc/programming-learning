"""
Pixora — Streamlit (Replit-style UI)
Run: streamlit run app.py

Note: Replit app is Next.js — 100% pixel match needs that stack.
This file gets ~85% look + same flows (auth, feed, DMs, Jitsi calls).
"""
import streamlit as st
import sqlite3
import hashlib
import datetime
import html
import base64
import io
import json
import re
from urllib.parse import quote

from PIL import Image
import streamlit.components.v1 as components
from streamlit_autorefresh import st_autorefresh

# =============================================================================
# PAGE
# =============================================================================
st.set_page_config(
    page_title="Pixora — Social Media",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

def pixora_css(hide_sidebar: bool = False):
    hide = (
        "section[data-testid='stSidebar'] { display: none !important; }"
        "[data-testid='collapsedControl'] { display: none !important; }"
        if hide_sidebar
        else ""
    )
    st.markdown(
        f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
{hide}

#MainMenu, footer, header {{ visibility: hidden; }}
[data-testid="stHeader"] {{ background: transparent; }}
.block-container {{
    padding-top: 0.75rem;
    padding-bottom: 5.5rem;
    max-width: 680px;
    color: #fafafa !important;
}}

.stApp {{
    background: #09090b !important;
    font-family: 'Inter', system-ui, sans-serif !important;
}}
.stApp, .stApp p, .stApp label, .stApp span,
[data-testid="stMarkdownContainer"], [data-testid="stMarkdownContainer"] p,
[data-testid="stWidgetLabel"], .stCaption {{
    color: #e4e4e7 !important;
}}
h1, h2, h3, h4, h5, h6 {{ color: #ffffff !important; }}

.stTextInput input, .stTextArea textarea {{
    background: #18181b !important;
    color: #ffffff !important;
    border: 1px solid #52525b !important;
    border-radius: 12px !important;
}}
.stTextInput label, .stTextArea label {{ color: #d4d4d8 !important; }}

.stButton > button {{
    background: #27272a !important;
    color: #ffffff !important;
    border: 1px solid #52525b !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
}}
.stButton > button[kind="primary"] {{
    background: linear-gradient(135deg, #7c3aed 0%, #c026d3 50%, #e11d48 100%) !important;
    border: none !important;
    color: #fff !important;
}}
.stLinkButton > a {{
    background: #4c1d95 !important;
    color: #fff !important;
    border-radius: 12px !important;
}}

[data-testid="stMetricValue"] {{ color: #fff !important; }}
[data-testid="stMetricLabel"] {{ color: #a1a1aa !important; }}
[data-testid="stExpander"] {{
    background: #18181b !important;
    border: 1px solid #27272a !important;
    border-radius: 12px !important;
}}
[data-testid="stVerticalBlockBorderWrapper"] {{
    background: #18181b !important;
    border-color: #27272a !important;
}}
.stAlert {{ background: #18181b !important; color: #e4e4e7 !important; border: 1px solid #3f3f46 !important; }}

.pixora-logo {{
    font-size: 1.75rem;
    font-weight: 800;
    letter-spacing: -0.04em;
    color: #fafafa;
    margin: 0;
}}
.pixora-logo span {{
    background: linear-gradient(90deg, #c4b5fd, #f0abfc, #fda4af);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}}
.hero-title {{
    font-size: clamp(2rem, 4vw, 3rem);
    font-weight: 800;
    line-height: 1.08;
    color: #fafafa !important;
    letter-spacing: -0.03em;
}}
.hero-sub {{
    color: #a1a1aa !important;
    font-size: 1.05rem;
    line-height: 1.65;
    max-width: 32rem;
}}
.auth-card {{
    background: #18181b;
    border: 1px solid #27272a;
    border-radius: 20px;
    padding: 0.25rem 0;
}}
.post-card {{
    background: #18181b;
    border: 1px solid #27272a;
    border-radius: 16px;
    overflow: hidden;
    margin-bottom: 1.25rem;
}}
.post-head {{
    padding: 14px 16px;
    font-weight: 600;
    font-size: 14px;
    color: #fafafa !important;
    border-bottom: 1px solid #27272a;
}}
.post-foot {{
    padding: 12px 16px 16px;
    font-size: 14px;
    color: #e4e4e7 !important;
}}
.call-strip {{
    background: linear-gradient(135deg, #1e1b4b, #4c1d95);
    color: #ede9fe !important;
    padding: 10px 14px;
    border-radius: 12px;
    margin-bottom: 10px;
    font-size: 14px;
    border: 1px solid #6d28d9;
}}
.call-strip.ringing {{ animation: pixPulse 1.5s infinite; }}
@keyframes pixPulse {{
    0%, 100% {{ box-shadow: 0 0 0 0 rgba(139, 92, 246, 0.45); }}
    50% {{ box-shadow: 0 0 0 10px rgba(139, 92, 246, 0); }}
}}

.top-bar {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0.5rem 0 1rem 0;
    border-bottom: 1px solid #27272a;
    margin-bottom: 1rem;
}}
.top-bar .user-pill {{
    font-size: 13px;
    color: #a1a1aa !important;
    background: #18181b;
    border: 1px solid #27272a;
    padding: 6px 12px;
    border-radius: 999px;
}}

.bottom-nav-wrap {{
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    z-index: 999;
    background: rgba(9, 9, 11, 0.92);
    backdrop-filter: blur(12px);
    border-top: 1px solid #27272a;
    padding: 0.35rem 0 max(0.35rem, env(safe-area-inset-bottom));
}}
.bottom-nav-wrap [data-testid="column"] {{
    padding: 0 2px !important;
}}
.bottom-nav-wrap .stButton > button {{
    background: transparent !important;
    border: none !important;
    font-size: 12px !important;
    padding: 8px 4px !important;
    color: #71717a !important;
}}
.bottom-nav-wrap .stButton > button[kind="primary"] {{
    background: #27272a !important;
    color: #fafafa !important;
    border-radius: 10px !important;
}}
</style>
""",
        unsafe_allow_html=True,
    )


pixora_css(hide_sidebar=False)

DB_FILE = "pixora_social.db"
IMG_LANDING = "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=1400&auto=format&fit=crop"
IMG_SIGNIN = "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=1400&auto=format&fit=crop"
IMG_SIGNUP = "https://images.unsplash.com/photo-1549490349-8643362247b5?q=80&w=1400&auto=format&fit=crop"


# =============================================================================
# DATABASE
# =============================================================================
def get_db():
    conn = sqlite3.connect(DB_FILE, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            handle TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            name TEXT,
            bio TEXT,
            avatar BLOB,
            last_seen TEXT
        );
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            handle TEXT,
            img_blob BLOB,
            caption TEXT,
            date TEXT
        );
        CREATE TABLE IF NOT EXISTS likes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            handle TEXT,
            post_id INTEGER,
            UNIQUE(handle, post_id)
        );
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender TEXT,
            receiver TEXT,
            content TEXT,
            timestamp TEXT,
            is_seen INTEGER DEFAULT 0,
            msg_type TEXT DEFAULT 'text',
            media_blob BLOB
        );
        CREATE TABLE IF NOT EXISTS followers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT,
            following TEXT,
            is_notified INTEGER DEFAULT 0,
            UNIQUE(user, following)
        );
        CREATE TABLE IF NOT EXISTS chats_calling (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            caller TEXT,
            receiver TEXT,
            call_type TEXT,
            status TEXT DEFAULT 'ringing'
        );
        """
    )
    conn.commit()
    conn.close()


init_db()


def hash_pass(password):
    return hashlib.sha256(password.encode()).hexdigest()


def touch(email):
    conn = get_db()
    conn.execute(
        "UPDATE users SET last_seen = ? WHERE email = ?",
        (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), email),
    )
    conn.commit()
    conn.close()


def normalize_handle(raw):
    h = (raw or "").strip().lower().lstrip("@")
    h = re.sub(r"[^a-z0-9._]", "", h)
    return h


def clear_session():
    for k in list(st.session_state.keys()):
        del st.session_state[k]


def require_valid_session():
    email = st.session_state.get("email", "")
    if not email:
        clear_session()
        st.rerun()
    row = get_db().execute("SELECT 1 FROM users WHERE email = ?", (email,)).fetchone()
    if not row:
        clear_session()
        st.warning("Session expired. Please sign in again.")
        st.rerun()


def jitsi_room(a, b):
    x, y = sorted([a, b])
    return quote(f"pixora_{x}_{y}")


def jitsi_url(caller, receiver, ctype):
    url = f"https://meet.jit.si/{jitsi_room(caller, receiver)}"
    if ctype == "audio":
        url += "#config.startWithVideoMuted=true&config.startAudioOnly=true"
    return url


def log_call(conn, sender, receiver, text):
    now = datetime.datetime.now().strftime("%I:%M %p")
    conn.execute(
        """
        INSERT INTO messages (sender, receiver, content, timestamp, msg_type, media_blob, is_seen)
        VALUES (?, ?, ?, ?, 'call', NULL, 1)
        """,
        (sender, receiver, text, now),
    )


def render_chat(messages_history, my_handle):
    items = []
    for msg in messages_history:
        mine = msg["sender"] == my_handle
        mtype = msg["msg_type"] or "text"
        if mtype == "call":
            items.append({
                "type": "call",
                "text": msg["content"] or "Call",
                "time": str(msg["timestamp"] or ""),
            })
            continue
        item = {
            "type": mtype if mtype in ("text", "image", "video", "audio") else "text",
            "side": "me" if mine else "them",
            "time": str(msg["timestamp"] or ""),
            "ticks": " ✓✓" if (mine and msg["is_seen"]) else (" ✓" if mine else ""),
            "text": msg["content"] or "",
        }
        if mtype == "image" and msg["media_blob"]:
            item["b64"] = base64.b64encode(msg["media_blob"]).decode()
            item["mime"] = "image/jpeg"
        elif mtype == "video" and msg["media_blob"]:
            item["b64"] = base64.b64encode(msg["media_blob"]).decode()
            item["mime"] = "video/mp4"
        elif mtype == "audio" and msg["media_blob"]:
            item["b64"] = base64.b64encode(msg["media_blob"]).decode()
            item["mime"] = "audio/mpeg"
        items.append(item)

    payload = json.dumps(items)
    components.html(
        f"""
<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>
  body {{ margin:0; font-family:Inter,sans-serif; background:#09090b; }}
  #chat-box {{
    height:400px; overflow-y:auto; display:flex; flex-direction:column-reverse;
    padding:12px; background:#18181b; border:1px solid #27272a; border-radius:14px; gap:8px;
  }}
  .row {{ display:flex; width:100%; }}
  .row.me {{ justify-content:flex-end; }}
  .row.them {{ justify-content:flex-start; }}
  .bubble {{
    max-width:72%; padding:10px 14px; border-radius:18px; font-size:14px; line-height:1.4;
  }}
  .bubble.me {{
    background:linear-gradient(135deg,#7c3aed,#c026d3); color:#fff;
    border-bottom-right-radius:4px;
  }}
  .bubble.them {{
    background:#27272a; color:#fafafa; border-bottom-left-radius:4px;
  }}
  .bubble img,.bubble video {{ max-width:220px; width:100%; border-radius:8px; display:block; }}
  .meta {{ font-size:10px; opacity:.7; margin-top:4px; text-align:right; }}
  .call-log {{
    align-self:center; background:#3b0764; color:#e9d5ff; font-size:12px;
    padding:6px 14px; border-radius:8px; text-align:center; max-width:92%; margin:4px auto;
  }}
  .call-log small {{ display:block; font-size:10px; opacity:.85; margin-top:2px; }}
</style></head>
<body>
<div id="chat-box"></div>
<script>
const messages = {payload};
const box = document.getElementById("chat-box");
function esc(s){{ return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;"); }}
function render(){{
  if(!messages.length){{ box.innerHTML="<p style='text-align:center;color:#71717a;margin-top:40px'>No messages yet</p>"; box.scrollTop=0; return; }}
  let html="";
  for(let i=messages.length-1;i>=0;i--){{
    const m=messages[i];
    if(m.type==="call"){{ html+=`<div class="call-log">${{esc(m.text)}}<small>${{esc(m.time)}}</small></div>`; continue; }}
    let body="";
    if(m.type==="text") body=esc(m.text);
    else if(m.b64) body=`<img src="data:${{m.mime}};base64,${{m.b64}}">`;
    else body=esc(m.text);
    html+=`<div class="row ${{m.side}}"><div class="bubble ${{m.side}}">${{body}}<div class="meta">${{esc(m.time)}}${{esc(m.ticks||"")}}</div></div></div>`;
  }}
  box.innerHTML=html; box.scrollTop=0;
}}
render(); setTimeout(()=>box.scrollTop=0,150);
</script>
</body></html>
        """,
        height=420,
        scrolling=False,
    )


def render_bottom_nav(unread: int, new_fol: int):
    page = st.session_state.page_key
    labels = [
        ("Home", "🏠"),
        ("Messages", f"💬{f' ·{unread}' if unread else ''}"),
        ("Explore", "🧭"),
        ("Profile", f"👤{f' ·{new_fol}' if new_fol else ''}"),
    ]
    st.markdown('<div class="bottom-nav-wrap">', unsafe_allow_html=True)
    cols = st.columns(4)
    for col, (key, icon_label) in zip(cols, labels):
        with col:
            active = page == key
            if st.button(icon_label, key=f"nav_{key}", use_container_width=True, type="primary" if active else "secondary"):
                st.session_state.page_key = key
                if key != "Messages":
                    st.session_state.active_chat = None
                st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)


# =============================================================================
# SESSION
# =============================================================================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "email" not in st.session_state:
    st.session_state.email = ""
if "handle" not in st.session_state:
    st.session_state.handle = ""
if "active_chat" not in st.session_state:
    st.session_state.active_chat = None
if "auth_page" not in st.session_state:
    st.session_state.auth_page = "landing"
if "page_key" not in st.session_state:
    st.session_state.page_key = "Home"


# =============================================================================
# AUTH (Replit landing copy)
# =============================================================================
if not st.session_state.logged_in:
    page = st.session_state.auth_page

    if page == "landing":
        st.markdown(
            '<p class="pixora-logo"><span>Pixora</span></p>',
            unsafe_allow_html=True,
        )
        left, right = st.columns([1.15, 1], gap="large")
        with left:
            st.markdown(
                '<p class="hero-title">Visual storytelling for creatives.</p>',
                unsafe_allow_html=True,
            )
            st.markdown(
                '<p class="hero-sub">A premium space to share your world. No noise, no algorithms '
                "optimizing for rage. Just beautiful images and the people who care about them.</p>",
                unsafe_allow_html=True,
            )
            b1, b2 = st.columns(2)
            if b1.button("Join Pixora", type="primary", use_container_width=True):
                st.session_state.auth_page = "signup"
                st.rerun()
            if b2.button("Log In", use_container_width=True):
                st.session_state.auth_page = "login"
                st.rerun()
        with right:
            st.image(IMG_LANDING, use_container_width=True)
        st.stop()

    is_login = page == "login"
    col_form, col_art = st.columns([1, 1.05], gap="large")

    with col_form:
        st.markdown('<p class="pixora-logo"><span>Pixora</span></p>', unsafe_allow_html=True)
        st.markdown(f"### {'Welcome back' if is_login else 'Create an account'}")
        st.caption(
            "Enter your details to sign in to your account."
            if is_login
            else "Join the creative community"
        )

        st.markdown('<div class="auth-card">', unsafe_allow_html=True)
        email = st.text_input("Email", placeholder="you@example.com").strip().lower()
        user_handle = ""
        display_name = ""
        if not is_login:
            user_handle = st.text_input("Username", placeholder="creative_handle").strip()
            display_name = st.text_input("Display Name", placeholder="Your name")
        password = st.text_input("Password", type="password")

        if st.button("Sign In" if is_login else "Sign Up", type="primary", use_container_width=True):
            if not email or not password or (not is_login and (not user_handle or not display_name)):
                st.warning("Please fill all required fields.")
            else:
                conn = get_db()
                hp = hash_pass(password)
                if is_login:
                    u = conn.execute(
                        "SELECT * FROM users WHERE email = ? AND password = ?",
                        (email, hp),
                    ).fetchone()
                    if u:
                        st.session_state.logged_in = True
                        st.session_state.email = u["email"]
                        st.session_state.handle = u["handle"]
                        st.session_state.auth_page = "landing"
                        st.session_state.page_key = "Home"
                        touch(email)
                        conn.close()
                        st.rerun()
                    st.error("Invalid email or password.")
                else:
                    h = normalize_handle(user_handle)
                    if len(h) < 3:
                        st.error("Username must be at least 3 characters (letters, numbers, . _)")
                    else:
                        try:
                            conn.execute(
                                "INSERT INTO users (email, handle, password, name, bio, last_seen) "
                                "VALUES (?, ?, ?, ?, ?, ?)",
                                (
                                    email,
                                    h,
                                    hp,
                                    display_name,
                                    "",
                                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                ),
                            )
                            conn.commit()
                            st.success("Account created! Please sign in.")
                            st.session_state.auth_page = "login"
                        except sqlite3.IntegrityError as e:
                            if "email" in str(e).lower():
                                st.error("Email already registered.")
                            else:
                                st.error("Username already taken.")
                conn.close()

        st.markdown("</div>", unsafe_allow_html=True)

        if is_login:
            if st.button("← Back"):
                st.session_state.auth_page = "landing"
                st.rerun()
        else:
            if st.button("Already have an account? Log in"):
                st.session_state.auth_page = "login"
                st.rerun()

    with col_art:
        st.image(IMG_SIGNIN if is_login else IMG_SIGNUP, use_container_width=True)

    st.stop()


# =============================================================================
# LOGGED IN — Replit-style shell (no sidebar, bottom nav)
# =============================================================================
require_valid_session()
pixora_css(hide_sidebar=True)

my_email = st.session_state.email
my_handle = st.session_state.handle
touch(my_email)

conn = get_db()
cur = conn.cursor()

unread = cur.execute(
    "SELECT COUNT(*) AS c FROM messages WHERE receiver = ? AND is_seen = 0 AND msg_type != 'call'",
    (my_handle,),
).fetchone()["c"]
new_fol = cur.execute(
    "SELECT COUNT(*) AS c FROM followers WHERE following = ? AND is_notified = 0",
    (my_handle,),
).fetchone()["c"]

urow = cur.execute(
    "SELECT avatar, name, handle FROM users WHERE email = ?", (my_email,)
).fetchone()
display_title = (urow["name"] if urow and urow["name"] else None) or (urow["handle"] if urow else my_handle)

st.markdown(
    f"""
<div class="top-bar">
  <p class="pixora-logo"><span>Pixora</span></p>
  <span class="user-pill">@{my_handle}</span>
</div>
""",
    unsafe_allow_html=True,
)

app_mode = st.session_state.page_key

# Poll incoming calls only on Messages (page stays put via page_key)
if app_mode == "Messages":
    st_autorefresh(interval=5000, key="messages_poll")

if app_mode == "Home":
    st.markdown("### Your feed")
    following = [
        r["following"]
        for r in cur.execute("SELECT following FROM followers WHERE user = ?", (my_handle,)).fetchall()
    ]
    following.append(my_handle)
    ph = ",".join("?" * len(following))
    posts = cur.execute(
        f"SELECT * FROM posts WHERE handle IN ({ph}) ORDER BY id DESC", following
    ).fetchall()

    if not posts:
        st.info("Follow creators in **Explore** to fill your feed.")
    else:
        for p in posts:
            pid = p["id"]
            owner = p["handle"]
            likes = cur.execute("SELECT COUNT(*) AS c FROM likes WHERE post_id = ?", (pid,)).fetchone()["c"]
            liked = cur.execute(
                "SELECT 1 FROM likes WHERE handle = ? AND post_id = ?", (my_handle, pid)
            ).fetchone()
            st.markdown(f"<div class='post-card'><div class='post-head'>@{owner}</div>", unsafe_allow_html=True)
            st.image(Image.open(io.BytesIO(p["img_blob"])), use_container_width=True)
            cap = html.escape(p["caption"] or "")
            st.markdown(
                f"<div class='post-foot'><b>{likes}</b> likes · {cap}"
                f"<br><span style='color:#71717a;font-size:12px'>{p['date']}</span></div></div>",
                unsafe_allow_html=True,
            )
            if st.button("♥ Liked" if liked else "♡ Like", key=f"lk_{pid}"):
                if liked:
                    conn.execute("DELETE FROM likes WHERE handle = ? AND post_id = ?", (my_handle, pid))
                else:
                    conn.execute("INSERT OR IGNORE INTO likes (handle, post_id) VALUES (?, ?)", (my_handle, pid))
                conn.commit()
                st.rerun()

elif app_mode == "Messages":
    left, right = st.columns([1, 2.2], gap="medium")
    with left:
        st.markdown("#### Messages")
        threads = [
            r["following"]
            for r in cur.execute("SELECT following FROM followers WHERE user = ?", (my_handle,)).fetchall()
        ]
        if not threads:
            st.info("Follow people in Explore.")
        for t in threads:
            n = cur.execute(
                "SELECT COUNT(*) AS c FROM messages WHERE sender = ? AND receiver = ? "
                "AND is_seen = 0 AND msg_type != 'call'",
                (t, my_handle),
            ).fetchone()["c"]
            lbl = ("▸ " if st.session_state.active_chat == t else "") + f"@{t}"
            if n:
                lbl += f" ({n})"
            if st.button(lbl, key=f"th_{t}", use_container_width=True):
                st.session_state.active_chat = t
                conn.execute(
                    "UPDATE messages SET is_seen = 1 WHERE sender = ? AND receiver = ?",
                    (t, my_handle),
                )
                conn.commit()
                st.rerun()

    with right:
        peer = st.session_state.active_chat
        if not peer:
            st.markdown(
                "<p style='text-align:center;color:#71717a;margin-top:120px'>Select a conversation</p>",
                unsafe_allow_html=True,
            )
        else:
            conn.execute(
                "UPDATE messages SET is_seen = 1 WHERE sender = ? AND receiver = ?",
                (peer, my_handle),
            )
            conn.commit()

            call = cur.execute(
                "SELECT * FROM chats_calling WHERE (caller = ? OR receiver = ?) AND status != 'ended'",
                (my_handle, my_handle),
            ).fetchone()

            if call:
                cid, cu, ru = call["id"], call["caller"], call["receiver"]
                ct, cs = call["call_type"], call["status"]
                other = cu if ru == my_handle else ru
                url = jitsi_url(cu, ru, ct)

                if ru == my_handle and cs == "ringing":
                    st.markdown(
                        f"<div class='call-strip ringing'>📲 Incoming {ct} from @{cu}</div>",
                        unsafe_allow_html=True,
                    )
                    a1, a2 = st.columns(2)
                    if a1.button("Accept", type="primary", use_container_width=True, key="c_ok"):
                        conn.execute("UPDATE chats_calling SET status = 'connected' WHERE id = ?", (cid,))
                        log_call(conn, my_handle, peer, f"✅ {ct.capitalize()} call answered")
                        conn.commit()
                        st.rerun()
                    if a2.button("Decline", use_container_width=True, key="c_no"):
                        conn.execute("UPDATE chats_calling SET status = 'ended' WHERE id = ?", (cid,))
                        log_call(conn, cu, my_handle, f"❌ Missed {ct} call")
                        conn.commit()
                        st.rerun()
                elif cu == my_handle and cs == "ringing":
                    st.markdown(f"<div class='call-strip'>📞 Calling @{ru}…</div>", unsafe_allow_html=True)
                    if st.button("Cancel", use_container_width=True, key="c_cancel"):
                        conn.execute("UPDATE chats_calling SET status = 'ended' WHERE id = ?", (cid,))
                        log_call(conn, my_handle, peer, f"📴 {ct.capitalize()} call cancelled")
                        conn.commit()
                        st.rerun()
                elif cs == "connected":
                    st.markdown(
                        f"<div class='call-strip'>🟢 Live {ct} with @{other}</div>",
                        unsafe_allow_html=True,
                    )
                    j1, j2 = st.columns(2)
                    j1.link_button("Join call (tab)", url, use_container_width=True)
                    if j2.button("End", use_container_width=True, key="c_end"):
                        conn.execute("UPDATE chats_calling SET status = 'ended' WHERE id = ?", (cid,))
                        log_call(conn, my_handle, peer, f"📴 {ct.capitalize()} call ended")
                        conn.commit()
                        st.rerun()
                    with st.expander("Preview (demo)", expanded=False):
                        components.iframe(url, height=160)

            hl, hr = st.columns([3, 1])
            hl.markdown(f"### @{peer}")
            c1, c2 = hr.columns(2)
            if c1.button("📞", key="audio"):
                conn.execute("DELETE FROM chats_calling WHERE caller = ?", (my_handle,))
                conn.execute(
                    "INSERT INTO chats_calling (caller, receiver, call_type, status) VALUES (?, ?, 'audio', 'ringing')",
                    (my_handle, peer),
                )
                log_call(conn, my_handle, peer, "📞 Voice call started")
                conn.commit()
                st.rerun()
            if c2.button("📹", key="video"):
                conn.execute("DELETE FROM chats_calling WHERE caller = ?", (my_handle,))
                conn.execute(
                    "INSERT INTO chats_calling (caller, receiver, call_type, status) VALUES (?, ?, 'video', 'ringing')",
                    (my_handle, peer),
                )
                log_call(conn, my_handle, peer, "📹 Video call started")
                conn.commit()
                st.rerun()

            hist = cur.execute(
                """
                SELECT * FROM messages
                WHERE (sender = ? AND receiver = ?) OR (sender = ? AND receiver = ?)
                ORDER BY id ASC
                """,
                (my_handle, peer, peer, my_handle),
            ).fetchall()
            render_chat(hist, my_handle)

            with st.form("send", clear_on_submit=True):
                txt = st.text_input("m", placeholder="Message…", label_visibility="collapsed")
                with st.expander("Attach"):
                    fi = st.file_uploader("Photo", type=["jpg", "jpeg", "png"], key="ci")
                    fv = st.file_uploader("Video", type=["mp4"], key="cv")
                if st.form_submit_button("Send", use_container_width=True):
                    ts = datetime.datetime.now().strftime("%I:%M %p")
                    if fi:
                        conn.execute(
                            "INSERT INTO messages (sender, receiver, content, timestamp, msg_type, media_blob) "
                            "VALUES (?, ?, '📷 Photo', ?, 'image', ?)",
                            (my_handle, peer, ts, fi.read()),
                        )
                    elif fv:
                        conn.execute(
                            "INSERT INTO messages (sender, receiver, content, timestamp, msg_type, media_blob) "
                            "VALUES (?, ?, '📹 Video', ?, 'video', ?)",
                            (my_handle, peer, ts, fv.read()),
                        )
                    elif txt.strip():
                        conn.execute(
                            "INSERT INTO messages (sender, receiver, content, timestamp, msg_type, media_blob) "
                            "VALUES (?, ?, ?, ?, 'text', NULL)",
                            (my_handle, peer, txt.strip(), ts),
                        )
                    conn.commit()
                    st.rerun()

elif app_mode == "Profile":
    conn.execute("UPDATE followers SET is_notified = 1 WHERE following = ?", (my_handle,))
    conn.commit()
    user = cur.execute("SELECT * FROM users WHERE email = ?", (my_email,)).fetchone()
    if not user:
        require_valid_session()

    pc = cur.execute("SELECT COUNT(*) AS c FROM posts WHERE handle = ?", (my_handle,)).fetchone()["c"]
    fol = [r["user"] for r in cur.execute("SELECT user FROM followers WHERE following = ?", (my_handle,)).fetchall()]
    fing = [r["following"] for r in cur.execute("SELECT following FROM followers WHERE user = ?", (my_handle,)).fetchall()]

    p1, p2 = st.columns([1, 2])
    with p1:
        if user["avatar"]:
            st.image(Image.open(io.BytesIO(user["avatar"])), width=140)
        else:
            st.image("https://www.w3schools.com/howto/img_avatar.png", width=140)
    with p2:
        st.markdown(f"## {user['name'] or user['handle']}")
        st.caption(f"@{user['handle']} · {user['email']}")
        m1, m2, m3 = st.columns(3)
        m1.metric("Posts", pc)
        m2.metric("Followers", len(fol))
        m3.metric("Following", len(fing))
        st.write(user["bio"] or "No bio yet.")

    with st.expander("Edit profile"):
        av = st.file_uploader("Avatar", type=["jpg", "jpeg", "png"])
        nm = st.text_input("Display name", value=user["name"] or "")
        bi = st.text_area("Bio", value=user["bio"] or "")
        if st.button("Save"):
            if av:
                conn.execute(
                    "UPDATE users SET name=?, bio=?, avatar=? WHERE email=?",
                    (nm, bi, av.read(), my_email),
                )
            else:
                conn.execute("UPDATE users SET name=?, bio=? WHERE email=?", (nm, bi, my_email))
            conn.commit()
            st.rerun()
        if st.button("Log out", use_container_width=True):
            clear_session()
            st.rerun()

    st.divider()
    up = st.file_uploader("Upload photo", type=["jpg", "jpeg", "png"], key="newpost")
    cap = st.text_area("Caption")
    if st.button("Publish", type="primary") and up and cap:
        conn.execute(
            "INSERT INTO posts (handle, img_blob, caption, date) VALUES (?, ?, ?, ?)",
            (my_handle, up.read(), cap, str(datetime.date.today())),
        )
        conn.commit()
        st.success("Published!")
        st.rerun()

    grid = cur.execute("SELECT * FROM posts WHERE handle = ? ORDER BY id DESC", (my_handle,)).fetchall()
    if grid:
        cols = st.columns(3)
        for i, g in enumerate(grid):
            with cols[i % 3]:
                st.image(Image.open(io.BytesIO(g["img_blob"])), use_container_width=True)

else:
    st.markdown("### Discover creators")
    for u in cur.execute(
        "SELECT email, handle, name, bio FROM users WHERE handle != ?", (my_handle,)
    ).fetchall():
        h = u["handle"]
        is_fol = cur.execute(
            "SELECT 1 FROM followers WHERE user = ? AND following = ?", (my_handle, h)
        ).fetchone()
        with st.container(border=True):
            st.markdown(f"**{u['name'] or h}**")
            st.caption(f"@{h} · {u['bio'] or 'No bio'}")
            if is_fol:
                if st.button("Unfollow", key=f"un_{h}", use_container_width=True):
                    conn.execute("DELETE FROM followers WHERE user = ? AND following = ?", (my_handle, h))
                    conn.commit()
                    st.rerun()
            elif st.button("Follow", key=f"fo_{h}", use_container_width=True):
                conn.execute(
                    "INSERT OR IGNORE INTO followers (user, following, is_notified) VALUES (?, ?, 0)",
                    (my_handle, h),
                )
                conn.commit()
                st.rerun()

render_bottom_nav(unread, new_fol)
conn.close()
