import streamlit as st

st.set_page_config(page_title="streamlit-folium documentation")

"# streamlit-folium"

with st.echo():

    import streamlit as st
    from streamlit_folium import folium_static
    import folium

    page = st.radio("Select map type", ["Single map", "Dual map"], index=0)

    # center on Liberty Bell
    if page == "Single map":
        m = folium.Map(location=[47.574861376075134,7.635203190991693], zoom_start=16)

    # add marker for Liberty Bell
    tooltip = "Liberty Bell"
    folium.Marker(
        [47.574861376075134,7.635203190991693], popup="Liberty Bell", tooltip=tooltip
    ).add_to(m)
    folium.Marker(
        [39.9, -75.1], popup="test Bell", tooltip=tooltip
    ).add_to(m)
    folium.Marker(
        [39.949, -75.150], popup="test2 Bell", tooltip=tooltip
    ).add_to(m)

    # call to render Folium map in Streamlit
    folium_static(m)
