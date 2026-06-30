import streamlit as st
import numpy as np
import tensorly as tl
import pandas as pd

st.set_page_config(page_title="Математична Педагогіка", layout="wide")

st.title("🏛️ Математична Педагогіка: Тензорна Платформа")

# Инициализация тензора (Студент x 8 Книг x 3 Инструмента)
if 'student_tensor' not in st.session_state:
    st.session_state.student_tensor = np.random.rand(1, 8, 3)

# Список ваших 8 пособий
book_names = [
    "1. Три титани (Піфагор, Евклід, Архімед)",
    "2. Матаналіз (від Лейбніца до Ейлера)",
    "3. Незвідані глибини чисел (Ферма, Гаусс)",
    "4. Дискретний світ (Кантор, Гедель, Тюринг)",
    "5. Нова геометрія (Ріман, Пуанкаре)",
    "6. Статистика за келихом пива",
    "7. На межі відкриттів (Ріман, фон Нейман)",
    "8. Диференціальні рівняння (Ефект метелика)"
]

# Sidebar
st.sidebar.header("🎓 Траєкторія навчання")
# Простая логика рекомендации: находим раздел с самым низким баллом
scores = np.mean(st.session_state.student_tensor[0], axis=1)
recommended_idx = np.argmin(scores)

st.sidebar.success(f"Рекомендовано зараз:\n{book_names[recommended_idx]}")

page = st.sidebar.selectbox("Оберіть розділ книги:", book_names, index=recommended_idx)

# Основной интерфейс
col1, col2 = st.columns([2, 1])

with col1:
    st.header(f"📖 {page}")
    st.write("Тут буде розміщено інтерактивний зміст вашого посібника.")
    
    st.subheader("📊 Візуалізація (Desmos)")
    st.components.v1.html("""
        <iframe src="https://www.desmos.com/calculator/ptpbe99y32?embed" 
        width="100%" height="450" style="border: 1px solid #ccc" frameborder=0></iframe>
    """, height=470)

with col2:
    st.subheader("🧠 Тензорний профіль")
    st.write("Поточний стан компетентності:")
    
    # Срез тензора для выбранной книги
    current_book_idx = book_names.index(page)
    book_scores = st.session_state.student_tensor[0][current_book_idx]
    
    df = pd.DataFrame(book_scores, index=["Desmos", "Python", "R"], columns=["Рівень"])
    st.bar_chart(df)
    
    st.subheader("💻 Vibe-coding (AI)")
    prompt = st.text_input("Запит до ШІ (напр. 'побудуй графік...'):")
    if st.button("Згенерувати алгоритм"):
        st.code(f"# Алгоритм для {page}\nimport numpy as np\n# Обчислення через Python...")

st.divider()
st.caption("Розроблено в межах докторського дослідження зі спеціальності 13.00.04")
