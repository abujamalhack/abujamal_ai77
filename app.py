
import streamlit as st
import random
from datetime import datetime
from utils.responses import get_ai_responses

# إعدادات الصفحة
st.set_page_config(
    page_title="ذكاء اصطناعي - أبو جمال عبدالناصر الشوكي",
    page_icon="🤖",
    layout="wide"
)

# استدعاء الردود
responses_dict = get_ai_responses()

# تخصيص التصميم
with open("assets/style.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

# الهوية الشخصية
st.markdown('<div class="main-header">🤖 ذكاء اصطناعي حصري</div>', unsafe_allow_html=True)
st.markdown('<div class="creator-name">من صناعة أبو جمال عبدالناصر الشوكي</div>', unsafe_allow_html=True)
st.markdown("---")

# ذاكرة المحادثة
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "مرحباً بك! أنا مساعدك الذكي من صناعة **أبو جمال عبدالناصر الشوكي** 🌟"}
    ]

# شريط جانبي
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712109.png", width=100)
    st.title("معلومات المطور")
    st.write("**الاسم:** أبو جمال عبدالناصر الشوكي")
    st.write("**التخصص:** تطوير الذكاء الاصطناعي والأمن السيبراني")
    st.markdown("---")
    st.write("🕒 تم الإنشاء في: {}".format(datetime.now().strftime("%Y-%m-%d")))

    # زر إعادة تعيين المحادثة
    if st.button("🔄 مسح المحادثة"):
        st.session_state.messages = [
            {"role": "assistant", "content": "تم مسح المحادثة ✨ أهلاً بك من جديد!"}
        ]
        st.experimental_rerun()

    # عداد الرسائل
    st.write(f"📩 عدد الرسائل: {len(st.session_state.messages)}")

    # وضع ليلي/نهاري
    theme = st.radio("اختر النمط:", ["🌞 نهاري", "🌙 ليلي"])
    if theme == "🌙 ليلي":
        st.markdown("""
        <style>
            body, .stApp { background-color: #1e1e1e; color: #eee; }
            .main-header { color: #9b59b6 !important; }
            .creator-name { color: #f39c12 !important; }
        </style>
        """, unsafe_allow_html=True)

# عرض المحادثة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(f'<div class="arabic-text">{message["content"]}</div>', unsafe_allow_html=True)

# وظيفة توليد الردود
def generate_response(user_input):
    if any(word in user_input.lower() for word in ['اسمك', 'من انت', 'هويتك']):
        return random.choice(responses_dict["creator"])
    elif any(word in user_input.lower() for word in ['شكرا', 'مرحبا', 'اهلا']):
        return random.choice(responses_dict["greetings"])
    elif any(word in user_input.lower() for word in ['مع السلامة', 'باي']):
        return random.choice(responses_dict["farewell"])
    elif any(word in user_input.lower() for word in ['حب', 'حبيب', 'قلبي']):
        return "أحبك في الله يا قلبي! 🤲 **أبو جمال عبدالناصر الشوكي** يرسل لك تحياته الحارة!"
    else:
        return f"سؤالك: {user_input}\nردي: هذا موضوع شيق من تطوير **أبو جمال عبدالناصر الشوكي** 🚀"

# مدخلات المحادثة
if prompt := st.chat_input("اكتب رسالتك هنا... 🌸"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(f'<div class="arabic-text">{prompt}</div>', unsafe_allow_html=True)
    
    with st.chat_message("assistant"):
        with st.spinner('جاري التفكير... 🌟'):
            response = generate_response(prompt)
            st.markdown(f'<div class="arabic-text">{response}</div>', unsafe_allow_html=True)
    st.session_state.messages.append({"role": "assistant", "content": response})

# قسم إضافي للميزات
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🎯 المميزات")
    st.write("• ذكاء اصطناعي متطور")
    st.write("• واجهة عربية أنيقة")
    st.write("• وضع ليلي/نهاري")

with col2:
    st.subheader("🚀 التقنيات")
    st.write("• Python + Streamlit")
    st.write("• معالجة اللغة الطبيعية")
    st.write("• تصميم متجاوب")

with col3:
    st.subheader("📞 التواصل")
    st.write("المطور: أبو جمال عبدالناصر الشوكي")
    st.write("نوع المشروع: ذكاء اصطناعي")
    st.write("الترخيص: مفتوح المصدر")

# تذييل
st.markdown("---")
st.markdown('<div style="text-align: center; color: #666;">© 2025 جميع الحقوق محفوظة - تطوير أبو جمال عبدالناصر الشوكي 🌸</div>', unsafe_allow_html=True)
