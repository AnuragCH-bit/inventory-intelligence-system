import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/agent"

st.set_page_config(
    page_title="AI Procurement Copilot",
    page_icon="📦",
    layout="wide"
)

st.title("📦 AI Procurement Copilot")
st.write("Ask AI about inventory and procurement.")

sku = st.text_input(
    "SKU",
    value="BRG-0005"
)

question = st.text_area(
    "Question",
    value="Should I reorder this item?"
)

if st.button("Ask AI"):

    payload = {
        "sku": sku,
        "question": question
    }

    with st.spinner("Thinking..."):

        try:

            response = requests.post(
                API_URL,
                json=payload
            )

            # Debugging
            st.write("Status Code:", response.status_code)
            st.write("Response Text:")
            st.code(response.text)

            if response.status_code != 200:
                st.error("API returned an error.")
                st.stop()

            result = response.json()

            if result["success"]:

                st.success("Recommendation Generated")

                output = result["result"]

                st.subheader("📌 Recommendation")
                st.write(output["recommendation"])

                col1, col2 = st.columns(2)

                with col1:
                    st.metric(
                        "Priority",
                        output["priority"]
                    )

                with col2:
                    st.metric(
                        "Confidence",
                        output["confidence"]
                    )

                st.subheader("📝 Reason")
                st.write(output["reason"])

                st.subheader("➡️ Next Action")
                st.write(output["next_action"])

            else:

                st.error(result["message"])

        except Exception as e:

            st.error(f"Error: {e}")