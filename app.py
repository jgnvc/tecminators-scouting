import streamlit as st
from datetime import datetime

# ============================================================
# TECMINATORS SCOUTING - FTC BIOBUZZ 2026-2027
# V1 - Match Scouting
# ============================================================

st.set_page_config(
    page_title="TecMinators Scouting",
    page_icon="🐝",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================================
# ESTILO
# ============================================================

st.markdown("""
<style>

    .block-container {
        max-width: 800px;
        padding-top: 1.5rem;
        padding-bottom: 4rem;
    }

    h1 {
        text-align: center;
        margin-bottom: 0.2rem;
    }

    .subtitle {
        text-align: center;
        color: #888;
        margin-bottom: 2rem;
    }

    .section {
        font-size: 1.55rem;
        font-weight: 700;
        margin-top: 2rem;
        margin-bottom: 0.8rem;
        border-bottom: 2px solid #444;
        padding-bottom: 0.35rem;
    }

    .counter-label {
        font-weight: 600;
        margin-bottom: 0.2rem;
    }

    div.stButton > button {
        min-height: 3rem;
        font-size: 1.05rem;
    }

    .metric-box {
        background: #1f2028;
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
        margin-top: 0.5rem;
    }

    .metric-title {
        font-size: 0.9rem;
        color: #aaa;
    }

    .metric-value {
        font-size: 1.7rem;
        font-weight: 700;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# FUNCIONES
# ============================================================

def counter(label, key, min_value=0, max_value=99):
    """
    Contador con botones - y +.
    """
    if key not in st.session_state:
        st.session_state[key] = 0

    st.markdown(f'<div class="counter-label">{label}</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        if st.button("−", key=f"{key}_minus", use_container_width=True):
            st.session_state[key] = max(
                min_value,
                st.session_state[key] - 1
            )

    with col2:
        st.markdown(
            f"""
            <div class="metric-box">
                <div class="metric-value">{st.session_state[key]}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        if st.button("+", key=f"{key}_plus", use_container_width=True):
            st.session_state[key] = min(
                max_value,
                st.session_state[key] + 1
            )

    return st.session_state[key]


def reset_match():
    """
    Borra los datos del match actual.
    """
    keys = [
        "match_number",
        "team_number",
        "auto_leave",
        "auto_hive_tips",
        "auto_cell_pollen",
        "auto_cell_nectar",
        "teleop_hive_tips",
        "teleop_cell_pollen",
        "teleop_cell_nectar",
        "teleop_flower_pollen",
        "teleop_flower_nectar",
        "teleop_garden_pollen",
        "teleop_garden_nectar",
        "teleop_park",
        "defense_attempts",
        "defense_effective",
    ]

    for key in keys:
        if key in st.session_state:
            del st.session_state[key]

    st.rerun()


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

st.markdown('<div class="section">Datos del Match</div>', unsafe_allow_html=True)

match_type = st.selectbox(
    "Tipo de Match",
    [
        "Práctica",
        "Qualification",
        "Playoff"
    ]
)

match_number = st.number_input(
    "Número de Match",
    min_value=1,
    step=1,
    value=1,
    key="match_number"
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
    value=1,
    key="team_number"
)

surrogate = st.checkbox("Surrogate")


# ============================================================
# AUTÓNOMO
# ============================================================

st.markdown('<div class="section">Autónomo</div>', unsafe_allow_html=True)

st.caption("30 segundos")

auto_leave = st.checkbox(
    "LEAVE",
    key="auto_leave"
)

auto_hive_tips = counter(
    "HIVE TIPS",
    "auto_hive_tips",
    max_value=20
)

auto_cell_pollen = counter(
    "POLLEN restante en CELL",
    "auto_cell_pollen",
    max_value=20
)

auto_cell_nectar = counter(
    "NECTAR restante en CELL",
    "auto_cell_nectar",
    max_value=20
)


# ============================================================
# TELEOP
# ============================================================

st.markdown('<div class="section">TeleOp</div>', unsafe_allow_html=True)

st.caption("2 minutos")

teleop_hive_tips = counter(
    "HIVE TIPS",
    "teleop_hive_tips",
    max_value=20
)

teleop_cell_pollen = counter(
    "POLLEN en CELL",
    "teleop_cell_pollen",
    max_value=40
)

teleop_cell_nectar = counter(
    "NECTAR en CELL",
    "teleop_cell_nectar",
    max_value=20
)


# ============================================================
# FLOWERS
# ============================================================

st.markdown('<div class="section">Flowers</div>', unsafe_allow_html=True)

teleop_flower_pollen = counter(
    "POLLEN en FLOWERS",
    "teleop_flower_pollen",
    max_value=40
)

teleop_flower_nectar = counter(
    "NECTAR en FLOWERS",
    "teleop_flower_nectar",
    max_value=20
)

bottom_nectar_bonus = counter(
    "Bottom NECTAR Bonus",
    "bottom_nectar_bonus",
    max_value=4
)

owned_flowers = counter(
    "FLOWERS propias",
    "owned_flowers",
    max_value=4
)


# ============================================================
# GARDEN
# ============================================================

st.markdown('<div class="section">Garden</div>', unsafe_allow_html=True)

teleop_garden_pollen = counter(
    "POLLEN en GARDEN",
    "teleop_garden_pollen",
    max_value=40
)

teleop_garden_nectar = counter(
    "NECTAR en GARDEN",
    "teleop_garden_nectar",
    max_value=20
)


# ============================================================
# END GAME
# ============================================================

st.markdown('<div class="section">End Game</div>', unsafe_allow_html=True)

teleop_park = st.checkbox(
    "PARK",
    key="teleop_park"
)


# ============================================================
# DEFENSA
# ============================================================

st.markdown('<div class="section">Defensa</div>', unsafe_allow_html=True)

played_defense = st.radio(
    "¿Jugó defensa?",
    ["No", "Sí"],
    horizontal=True
)

defense_attempts = counter(
    "Interacciones de defensa",
    "defense_attempts",
    max_value=30
)

defense_effective = counter(
    "Interacciones efectivas",
    "defense_effective",
    max_value=30
)

was_defended = st.radio(
    "¿Fue defendido?",
    ["No", "Sí"],
    horizontal=True
)


# ============================================================
# OBSERVACIONES
# ============================================================

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


# ============================================================
# COMENTARIOS
# ============================================================

st.markdown(
    '<div class="section">Comentarios</div>',
    unsafe_allow_html=True
)

comments = st.text_area(
    "Comentarios del Match",
    placeholder="Ej. Buen ciclo, falló el intake durante TeleOp...",
    height=120
)


# ============================================================
# RESUMEN
# ============================================================

st.markdown(
    '<div class="section">Resumen</div>',
    unsafe_allow_html=True
)

total_hive_tips = auto_hive_tips + teleop_hive_tips

st.write(f"**Equipo:** {team_number}")
st.write(f"**Alianza:** {alliance}")
st.write(f"**HIVE TIPS:** {total_hive_tips}")
st.write(f"**FLOWERS propias:** {owned_flowers}")
st.write(f"**PARK:** {'Sí' if teleop_park else 'No'}")


# ============================================================
# GUARDAR
# ============================================================

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
        "surrogate": surrogate,

        "auto_leave": auto_leave,
        "auto_hive_tips": auto_hive_tips,
        "auto_cell_pollen": auto_cell_pollen,
        "auto_cell_nectar": auto_cell_nectar,

        "teleop_hive_tips": teleop_hive_tips,
        "teleop_cell_pollen": teleop_cell_pollen,
        "teleop_cell_nectar": teleop_cell_nectar,

        "flower_pollen": teleop_flower_pollen,
        "flower_nectar": teleop_flower_nectar,
        "bottom_nectar_bonus": bottom_nectar_bonus,
        "owned_flowers": owned_flowers,

        "garden_pollen": teleop_garden_pollen,
        "garden_nectar": teleop_garden_nectar,

        "park": teleop_park,

        "played_defense": played_defense,
        "defense_attempts": defense_attempts,
        "defense_effective": defense_effective,
        "was_defended": was_defended,

        "speed": speed,
        "cycle": cycle,
        "reliability": reliability,
        "driver": driver,

        "comments": comments
    }

    st.success("Match registrado correctamente.")

    st.json(scouting_data)


# ============================================================
# RESET
# ============================================================

if st.button(
    "Borrar match actual",
    use_container_width=True
):
    reset_match()
