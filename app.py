import streamlit as st

st.set_page_config(page_title="AI Support Ticket Assistant",layout="wide")

st.title("AI Support Ticket Classifier and Troubleshooting Assistant")
st.write("A small LLM-assisted tool to classify technical support tickets and suggest troubleshooting steps")

ticket_text = st.text_area("Paste the customer support ticket text here:", height =200,placeholder="Example: After rotating the API token, our integration is failing with 401 unauthorized....")

if st.button("Analyze Ticket"):
    if not ticket_text.strip():
        st.warning("Please enter a support issue first.")
    else:
        st.subheader("Triage Result")
        st.write("Issue Category: API / Integration")
        st.write("Issue summary: sample summary will appear here")
        st.write("Likely Root cause: sample root cause will appear here")
        st.write("Troubleshooting Steps:")
        st.write("1.Check API token")
        st.write("2. Validate endpoint")
        st.write("3. Review recent configuration changes")
        st.write("Priority: High")
        st.write("Escalate Recommendation: Escalate if issue persists after credential validation")
