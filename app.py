import streamlit as st
from datetime import datetime

# ============================================================
# TECMINATORS SCOUTING
# FTC BIOBUZZ 2026-2027
# ============================================================

st.set_page_config(
    page_title="TecMinators Scouting",
    page_icon="🐝",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

.block-container {
    max-width: 800px;
    padding-top: 1.2rem;
    padding-bottom: 5rem;
}

h1 {
    text-align: center;
    margin-bottom: 0.1rem;
}

.subtitle {
    text-align: center;
    color: #888;
    margin-bottom: 1.8rem;
}

.section {
    font-size: 1.55rem;
    font-weight: 700;
    margin-top: 1.8rem;
    margin-bottom: 0.8rem;
    border-bottom: 2px solid #444;
    padding-bottom: 0.35rem;
}

.counter-title {
    font-weight: 600;
    margin-bottom: 0.2rem;
}

.counter-value {
    background: #262730;
    border-radius: 10px;
    min-height: 3rem;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.35rem;
    font-weight: 700;
}

.score-box {
    background: #262730;
    border-radius: 12px;
    padding: 1rem;
    margin: 0.4rem 0;
}

.score-row {
    display: flex;
    justify-content: space-between;
    font-size: 1.05rem;
    padding: 0.25rem 0;
}

.score-total {
    font-size: 1.5rem;
    font-weight: 800;
    border-top: 2px solid #555;
    margin-top: 0.5rem;
    padding-top: 0.5rem;
}

div.stButton > button {
    min-height: 3rem;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SESSION STATE
# ============================================================

DEFAULTS = {
    "auto_hive_tips": 0,
    "auto_cell_pollen": 0,
    "auto_cell_nectar": 0,
    "auto_park": False,

    "teleop_hive_tips": 0,
    "teleop_cell_pollen": 0,
    "teleop_cell_nectar": 0,

    "flower_pollen": 0,
    "flower_nectar": 0,
    "bottom_nectar_bonus": 0,
    "owned_flowers": 0,

    "garden_pollen": 0,
    "garden_nectar": 0,

    "teleop_park": False,

    "defense_attempts": 0,
    "defense_effective": 0,
}

for key, value in DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# COUNTER
# ============================================================

def counter(label, key, maximum=99):

    if key not in st.session_state:
        st.session_state[key] = 0

    st.markdown(
        f'<div class="counter-title">{label}</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns([1, 2, 1])

    with c1:
        if st.button(
            "−",
            key=f"{key}_minus",
            use_container_width=True
        ):
            st.session_state[key] = max(
                0,
                st.session_state[key] - 1
            )

    with c2:
        st.markdown(
            f"""
            <div class="counter-value">
                {st.session_state[key]}
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:
        if st.button(
            "+",
            key=f"{key}_plus",
            use_container_width=True
        ):
            st.session_state[key] = min(
                maximum,
                st.session_state[key] + 1
            )

    return st.session_state[key]


# ============================================================
# HEADER
# ============================================================

st.title("TECMINATORS")

st.markdown(
    '<div class="subtitle">FTC BIOBUZZ 2026–2027 · MATCH SCOUTING</div>',
    unsafe_allow_html=True
)


# ============================================================
# DATOS GENERALES
# ============================================================

st.markdown(
    '<div class="section">Datos del Match</div>',
    unsafe_allow_html=True
)

match_type = st.selectbox(
    "Tipo de Match",
    ["Práctica", "Qualification", "Playoff"]
)

match_number = st.number_input(
    "Número de Match",
    min_value=1,
    step=1,
    value=1
)

alliance = st.selectbox(
    "Alianza",
    ["RED", "BLUE"]
)

position = st.selectbox(
    "Posición",
    ["1", "2"]
)

team_number = st.number_input(
    "Número de equipo",
    min_value=1,
    max_value=99999,
    step=1,
    value=1
)


# ============================================================
# SCOUTING FRAGMENT
# ============================================================

@st.fragment
def scouting():

    # ========================================================
    # AUTO
    # ========================================================

    st.markdown(
        '<div class="section">Autónomo</div>',
        unsafe_allow_html=True
    )

    st.caption("30 segundos")

    auto_leave = st.checkbox(
        "LEAVE"
    )

    auto_hive_tips = counter(
        "HIVE TIPS",
        "auto_hive_tips",
        20
    )

    auto_cell_pollen = counter(
        "POLLEN restante en CELL",
        "auto_cell_pollen",
        20
    )

    auto_cell_nectar = counter(
        "NECTAR restante en CELL",
        "auto_cell_nectar",
        20
    )

    auto_park = st.checkbox(
        "PARK durante AUTO",
        key="auto_park"
    )


    # ========================================================
    # TELEOP
    # ========================================================

    st.markdown(
        '<div class="section">TeleOp</div>',
        unsafe_allow_html=True
    )

    st.caption("2 minutos")

    teleop_hive_tips = counter(
        "HIVE TIPS",
        "teleop_hive_tips",
        20
    )

    teleop_cell_pollen = counter(
        "POLLEN restante en CELL",
        "teleop_cell_pollen",
        20
    )

    teleop_cell_nectar = counter(
        "NECTAR restante en CELL",
        "teleop_cell_nectar",
        20
    )


    # ========================================================
    # FLOWERS
    # ========================================================

    st.markdown(
        '<div class="section">Flowers</div>',
        unsafe_allow_html=True
    )

    flower_pollen = counter(
        "POLLEN colocado en FLOWERS",
        "flower_pollen",
        40
    )

    flower_nectar = counter(
        "NECTAR colocado en FLOWERS",
        "flower_nectar",
        20
    )

    bottom_nectar_bonus = counter(
        "Bottom NECTAR Bonus",
        "bottom_nectar_bonus",
        4
    )

    owned_flowers = counter(
        "FLOWERS propias",
        "owned_flowers",
        4
    )


    # ========================================================
    # GARDEN
    # ========================================================

    st.markdown(
        '<div class="section">Garden</div>',
        unsafe_allow_html=True
    )

    garden_pollen = counter(
        "POLLEN en GARDEN",
        "garden_pollen",
        40
    )

    garden_nectar = counter(
        "NECTAR en GARDEN",
        "garden_nectar",
        20
    )


    # ========================================================
    # END GAME
    # ========================================================

    st.markdown(
        '<div class="section">End Game</div>',
        unsafe_allow_html=True
    )

    teleop_park = st.checkbox(
        "PARK durante TELEOP",
        key="teleop_park"
    )


    # ========================================================
    # DEFENSA
    # ========================================================

    st.markdown(
        '<div class="section">Defensa</div>',
        unsafe_allow_html=True
    )

    played_defense = st.radio(
        "¿Jugó defensa?",
        ["No", "Sí"],
        horizontal=True
    )

    defense_attempts = counter(
        "Interacciones de defensa",
        "defense_attempts",
        30
    )

    defense_effective = counter(
        "Interacciones efectivas",
        "defense_effective",
        30
    )

    was_defended = st.radio(
        "¿Fue defendido?",
        ["No", "Sí"],
        horizontal=True
    )


    # ========================================================
    # OBSERVACIONES
    # ========================================================

    st.markdown(
        '<div class="section">Observaciones</div>',
        unsafe_allow_html=True
    )

    speed = st.select_slider(
        "Velocidad",
        options=[1, 2, 3, 4, 5],
        value=3
    )

    cycle = st.select_slider(
        "Velocidad de ciclo",
        options=[1, 2, 3, 4, 5],
        value=3
    )

    reliability = st.select_slider(
        "Confiabilidad",
        options=[1, 2, 3, 4, 5],
        value=3
    )

    driver = st.select_slider(
        "Driver",
        options=[1, 2, 3, 4, 5],
        value=3
    )


    # ========================================================
    # COMENTARIOS
    # ========================================================

    st.markdown(
        '<div class="section">Comentarios</div>',
        unsafe_allow_html=True
    )

    comments = st.text_area(
        "Comentarios del Match",
        placeholder="Ej. Buen ciclo, falló el intake...",
        height=120
    )


    # ========================================================
    # SCORING
    # ========================================================

    # AUTO
    auto_score = (
        (3 if auto_leave else 0)
        + (5 if auto_park else 0)
        + (auto_hive_tips * 20)
    )

    # TELEOP
    teleop_score = (
        (5 if teleop_park else 0)
        + (teleop_hive_tips * 20)
    )

    # CELL
    cell_score = (
        (auto_cell_pollen + auto_cell_nectar
         + teleop_cell_pollen + teleop_cell_nectar) * 2
    )

    # FLOWERS
    flower_score = (
        bottom_nectar_bonus * 5
        + ((flower_pollen + flower_nectar) * 2)
    )

    # GARDEN
    garden_score = (
        (garden_pollen + garden_nectar) * 1
    )

    # TOTAL OBSERVADO
    total_score = (
        auto_score
        + teleop_score
        + cell_score
        + flower_score
        + garden_score
    )


    # ========================================================
    # SCORING FINAL
    # ========================================================

    st.markdown(
        '<div class="section">Scoring Final</div>',
        unsafe_allow_html=True
    )

    st.caption(
        "Puntuación observada/atribuida según las acciones registradas del robot."
    )

    st.markdown(
        f"""
        <div class="score-box">

            <div class="score-row">
                <span>AUTÓNOMO</span>
                <strong>{auto_score}</strong>
            </div>

            <div class="score-row">
                <span>TELEOP</span>
                <strong>{teleop_score}</strong>
            </div>

            <div class="score-row">
                <span>CELL</span>
                <strong>{cell_score}</strong>
            </div>

            <div class="score-row">
                <span>FLOWERS</span>
                <strong>{flower_score}</strong>
            </div>

            <div class="score-row">
                <span>GARDEN</span>
                <strong>{garden_score}</strong>
            </div>

            <div class="score-row score-total">
                <span>TOTAL</span>
                <strong>{total_score}</strong>
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    # ========================================================
    # GUARDAR
    # ========================================================

    st.markdown("")

    if st.button(
        "GUARDAR MATCH",
        type="primary",
        use_container_width=True
    ):

        scouting_data = {
            "timestamp": datetime.now().isoformat(),

            "match_type": match_type,
            "match_number": match_number,
            "alliance": alliance,
            "position": position,
            "team_number": team_number,

            "auto_leave": auto_leave,
            "auto_park": auto_park,
            "auto_hive_tips": auto_hive_tips,
            "auto_cell_pollen": auto_cell_pollen,
            "auto_cell_nectar": auto_cell_nectar,

            "teleop_hive_tips": teleop_hive_tips,
            "teleop_cell_pollen": teleop_cell_pollen,
            "teleop_cell_nectar": teleop_cell_nectar,

            "flower_pollen": flower_pollen,
            "flower_nectar": flower_nectar,
            "bottom_nectar_bonus": bottom_nectar_bonus,
            "owned_flowers": owned_flowers,

            "garden_pollen": garden_pollen,
            "garden_nectar": garden_nectar,

            "teleop_park": teleop_park,

            "played_defense": played_defense,
            "defense_attempts": defense_attempts,
            "defense_effective": defense_effective,
            "was_defended": was_defended,

            "speed": speed,
            "cycle": cycle,
            "reliability": reliability,
            "driver": driver,

            "auto_score": auto_score,
            "teleop_score": teleop_score,
            "cell_score": cell_score,
            "flower_score": flower_score,
            "garden_score": garden_score,
            "total_score": total_score,

            "comments": comments
        }

        st.success("Match registrado correctamente.")

        st.json(scouting_data)


scouting()
