import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# =========================================================
# CONFIGURACIÓN
# =========================================================

st.set_page_config(
    page_title="TecMinators Scouting",
    page_icon="",
    layout="centered"
)

# =========================================================
# GOOGLE SHEETS
# =========================================================

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]


@st.cache_resource
def conectar_google_sheets():

    credentials = Credentials.from_service_account_info(
        dict(st.secrets["gcp_service_account"]),
        scopes=SCOPES
    )

    client = gspread.authorize(credentials)

    spreadsheet = client.open_by_key(
        "1sGoESN2GVpw_n_Y32VvcA5ROYNCy_SCTuFZ8--ifwVw"
    )

    worksheet = spreadsheet.sheet1

    return worksheet


# =========================================================
# ESTILOS
# =========================================================

st.markdown("""
<style>

.block-container {
    max-width: 700px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1 {
    text-align: center;
}

h2 {
    margin-top: 1.5rem;
}

.section {
    background-color: #1f2028;
    padding: 18px;
    border-radius: 14px;
    margin-bottom: 18px;
}

.score-total {
    background-color: #242630;
    border-radius: 15px;
    padding: 25px;
    text-align: center;
    font-size: 25px;
    font-weight: bold;
    margin-top: 20px;
    margin-bottom: 20px;
}

.score-total strong {
    font-size: 32px;
}

div.stButton > button {
    min-height: 45px;
    font-size: 18px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# TÍTULO
# =========================================================

st.title("TecMinators Scouting")
st.caption("FTC BIOBUZZ 2026–2027")


# =========================================================
# SESSION STATE
# =========================================================

defaults = {
    "auto_hive_tips": 0,
    "auto_cell_pollen": 0,
    "auto_cell_nectar": 0,
    "teleop_hive_tips": 0,
    "teleop_cell_pollen": 0,
    "teleop_cell_nectar": 0,
    "flower_pollen": 0,
    "flower_nectar": 0,
    "bottom_nectar_bonus": 0,
    "owned_flowers": 0,
    "garden_pollen": 0,
    "garden_nectar": 0,
    "defense_attempts": 0,
    "defense_effective": 0,
}

for key, value in defaults.items():

    if key not in st.session_state:
        st.session_state[key] = value


# =========================================================
# FUNCIÓN COUNTER
# =========================================================

def counter(label, key, min_value=0):

    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:

        if st.button(
            "−",
            key=f"{key}_minus",
            use_container_width=True
        ):

            if st.session_state[key] > min_value:
                st.session_state[key] -= 1

    with col2:

        st.markdown(
            f"""
            <div style="
                text-align:center;
                font-size:24px;
                font-weight:bold;
                padding-top:6px;
            ">
                {label}<br>
                <span style="font-size:30px;">
                    {st.session_state[key]}
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        if st.button(
            "+",
            key=f"{key}_plus",
            use_container_width=True
        ):

            st.session_state[key] += 1


# =========================================================
# DATOS GENERALES
# =========================================================

st.header("Datos del Match")

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
    step=1
)

col1, col2 = st.columns(2)

with col1:

    alliance = st.selectbox(
        "Alliance",
        ["RED", "BLUE"]
    )

with col2:

    position = st.selectbox(
        "Posición",
        [1, 2]
    )

# =========================================================
# POSICIÓN INICIAL
# =========================================================

st.subheader("Posición Inicial")

st.image(
    "field_positions.png",
    use_container_width=True
)

st.caption(
    "Selecciona la posición en la que inició el robot."
)

team_number = st.number_input(
    "Número de equipo",
    min_value=1,
    step=1
)


# =========================================================
# AUTO
# =========================================================

@st.fragment
def auto_section():

    st.header("AUTO")

    st.markdown(
        '<div class="section">',
        unsafe_allow_html=True
    )

    leave = st.checkbox("LEAVE")

    counter(
        "HIVE TIPS",
        "auto_hive_tips"
    )

    counter(
        "POLLEN restante en CELL",
        "auto_cell_pollen"
    )

    counter(
        "NECTAR restante en CELL",
        "auto_cell_nectar"
    )

    auto_park = st.checkbox(
        "PARK durante AUTO"
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

    return leave, auto_park


leave, auto_park = auto_section()


# =========================================================
# TELEOP
# =========================================================

@st.fragment
def teleop_section():

    st.header("TELEOP")

    st.markdown(
        '<div class="section">',
        unsafe_allow_html=True
    )

    counter(
        "HIVE TIPS",
        "teleop_hive_tips"
    )

    counter(
        "POLLEN restante en CELL",
        "teleop_cell_pollen"
    )

    counter(
        "NECTAR restante en CELL",
        "teleop_cell_nectar"
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


teleop_section()


# =========================================================
# FLOWERS
# =========================================================

@st.fragment
def flowers_section():

    st.header("FLOWERS")

    st.markdown(
        '<div class="section">',
        unsafe_allow_html=True
    )

    counter(
        "POLLEN colocado en FLOWERS",
        "flower_pollen"
    )

    counter(
        "NECTAR colocado en FLOWERS",
        "flower_nectar"
    )

    counter(
        "Bottom NECTAR Bonus",
        "bottom_nectar_bonus"
    )

    counter(
        "FLOWERS propias",
        "owned_flowers"
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


flowers_section()


# =========================================================
# GARDEN
# =========================================================

@st.fragment
def garden_section():

    st.header("GARDEN")

    st.markdown(
        '<div class="section">',
        unsafe_allow_html=True
    )

    counter(
        "POLLEN en GARDEN",
        "garden_pollen"
    )

    counter(
        "NECTAR en GARDEN",
        "garden_nectar"
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


garden_section()


# =========================================================
# END GAME
# =========================================================

st.header("END GAME")

st.markdown(
    '<div class="section">',
    unsafe_allow_html=True
)

teleop_park = st.checkbox(
    "PARK durante TELEOP"
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# DEFENSA
# =========================================================

@st.fragment
def defense_section():

    st.header("DEFENSA")

    st.markdown(
        '<div class="section">',
        unsafe_allow_html=True
    )

    played_defense = st.radio(
        "¿Jugó defensa?",
        ["Sí", "No"],
        horizontal=True
    )

    if played_defense == "Sí":

        counter(
            "Interacciones defensivas",
            "defense_attempts"
        )

        counter(
            "Interacciones efectivas",
            "defense_effective"
        )

    was_defended = st.radio(
        "¿El robot recibió defensa?",
        ["Sí", "No"],
        horizontal=True
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

    return played_defense, was_defended


played_defense, was_defended = defense_section()


# =========================================================
# OBSERVACIONES
# =========================================================

st.header("Observaciones")

st.markdown(
    '<div class="section">',
    unsafe_allow_html=True
)

speed = st.slider(
    "Velocidad",
    min_value=1,
    max_value=5,
    value=3
)

cycle_speed = st.slider(
    "Velocidad de ciclos",
    min_value=1,
    max_value=5,
    value=3
)

reliability = st.slider(
    "Confiabilidad",
    min_value=1,
    max_value=5,
    value=3
)

driver = st.slider(
    "Driver",
    min_value=1,
    max_value=5,
    value=3
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# COMENTARIOS
# =========================================================

st.header("Comentarios")

comments = st.text_area(
    "Comentarios del Scout",
    placeholder="Escribe aquí cualquier observación importante...",
    height=120
)


# =========================================================
# CÁLCULO DE SCORING
# =========================================================

auto_score = 0

if leave:
    auto_score += 3

if auto_park:
    auto_score += 5

auto_score += (
    st.session_state.auto_hive_tips * 20
)


teleop_score = 0

if teleop_park:
    teleop_score += 5

teleop_score += (
    st.session_state.teleop_hive_tips * 20
)


cell_score = (
    st.session_state.auto_cell_pollen
    + st.session_state.auto_cell_nectar
    + st.session_state.teleop_cell_pollen
    + st.session_state.teleop_cell_nectar
) * 2


flower_score = (
    st.session_state.bottom_nectar_bonus * 5
    + (
        st.session_state.flower_pollen
        + st.session_state.flower_nectar
    ) * 2
)


garden_score = (
    st.session_state.garden_pollen
    + st.session_state.garden_nectar
)


total_score = (
    auto_score
    + teleop_score
    + cell_score
    + flower_score
    + garden_score
)


# =========================================================
# SCORING FINAL
# =========================================================

st.header("Scoring Final")

st.markdown(
    f"""
    <div class="score-total">
        Scoring final solo Robot:
        <strong>{total_score} ptos</strong>
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# DATOS A GUARDAR
# =========================================================

scouting_data = {

    "match_type": match_type,
    "match_number": match_number,
    "alliance": alliance,
    "position": position,
    "team_number": team_number,

    "auto_leave": leave,
    "auto_hive_tips": st.session_state.auto_hive_tips,
    "auto_cell_pollen": st.session_state.auto_cell_pollen,
    "auto_cell_nectar": st.session_state.auto_cell_nectar,
    "auto_park": auto_park,

    "teleop_hive_tips": st.session_state.teleop_hive_tips,
    "teleop_cell_pollen": st.session_state.teleop_cell_pollen,
    "teleop_cell_nectar": st.session_state.teleop_cell_nectar,

    "flower_pollen": st.session_state.flower_pollen,
    "flower_nectar": st.session_state.flower_nectar,
    "bottom_nectar_bonus": st.session_state.bottom_nectar_bonus,
    "owned_flowers": st.session_state.owned_flowers,

    "garden_pollen": st.session_state.garden_pollen,
    "garden_nectar": st.session_state.garden_nectar,

    "teleop_park": teleop_park,

    "played_defense": played_defense,
    "defense_attempts": st.session_state.defense_attempts,
    "defense_effective": st.session_state.defense_effective,
    "was_defended": was_defended,

    "speed": speed,
    "cycle_speed": cycle_speed,
    "reliability": reliability,
    "driver": driver,

    "comments": comments,

    "scoring_final_robot": total_score
}


# =========================================================
# GUARDAR EN GOOGLE SHEETS
# =========================================================

st.header("Guardar Scouting")

if st.button(
    "GUARDAR MATCH",
    type="primary",
    use_container_width=True
):

    try:

        worksheet = conectar_google_sheets()

        row = [
            scouting_data["match_type"],
            scouting_data["match_number"],
            scouting_data["alliance"],
            scouting_data["position"],
            scouting_data["team_number"],

            scouting_data["auto_leave"],
            scouting_data["auto_hive_tips"],
            scouting_data["auto_cell_pollen"],
            scouting_data["auto_cell_nectar"],
            scouting_data["auto_park"],

            scouting_data["teleop_hive_tips"],
            scouting_data["teleop_cell_pollen"],
            scouting_data["teleop_cell_nectar"],

            scouting_data["flower_pollen"],
            scouting_data["flower_nectar"],
            scouting_data["bottom_nectar_bonus"],
            scouting_data["owned_flowers"],

            scouting_data["garden_pollen"],
            scouting_data["garden_nectar"],

            scouting_data["teleop_park"],

            scouting_data["played_defense"],
            scouting_data["defense_attempts"],
            scouting_data["defense_effective"],
            scouting_data["was_defended"],

            scouting_data["speed"],
            scouting_data["cycle_speed"],
            scouting_data["reliability"],
            scouting_data["driver"],

            scouting_data["comments"],

            scouting_data["scoring_final_robot"]
        ]

        worksheet.append_row(
            row,
            value_input_option="USER_ENTERED"
        )

        st.success(
            "Scouting guardado correctamente en Google Sheets."
        )

    except Exception as e:

        st.error(
            "No se pudo guardar el scouting."
        )

        st.exception(e)
