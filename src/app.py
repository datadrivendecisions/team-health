import streamlit as st
import plotly.graph_objs as go

# Define the attributes of a healthy team with descriptions
attributes_with_descriptions = {
    "Team Cohesion": "We have the mutual trust and respect necessary to be an effective team for healthy collaboration. We have a strong sense of connectedness between members.",
    "Balanced Team": "We have the right people, with the right skills, in the right clearly-defined roles. This enables us to successfully deliver the value for which this team is accountable.",
    "Encouraging Difference": "We seek and voice different viewpoints from diverse sources, both internally and externally, and we take the time to respectfully work through points of difference.",
    "Shared Understanding": "We share an understanding of our mission and purpose and our key milestones to deliver our strategic plan effectively as a team.",
    "Value and Metrics": "We understand the value we provide and the value back to the business, our definition of success and how that value is tracked and measured. We ultimately leverage our metrics to make decisions and action as necessary.",
    "Suitable Ways of Working": "Our ways of working together within the team enable us to do our jobs effectively, whether we are distributed or co-located. This includes the tools we use, how we meet and collaborate, and how we make decisions.",
    "Engagement and Support": "It's clear to other teams how and when to engage with us, teams do this effectively and consistently receive the support they need to progress. We have a clear understanding of who we depend on, and who depends on us.",
    "Continuous Improvement": "We always make time to celebrate our successes as well as earnestly reflect on, take action against, and fulfill our improvement opportunities. We have regular and intentional feedback loops within and outside of the team to make improvement decisions."
}

def make_spider_chart(values, attribute_labels, title):
    # Number of variables we're plotting.
    num_vars = len(attribute_labels)

    # Compute angle for each category
    angles = [(i / float(num_vars) * 360) for i in range(num_vars)]
    angles += angles[:1]  # complete the loop

    # The plotly go.Polar function needs to have the values repeated for the first value at the end to close the radar chart.
    values += values[:1]

    # Create radar chart
    fig = go.Figure(data=[
        go.Scatterpolar(
            r=values,
            theta=attribute_labels,
            fill='toself',
            name='Team Health'
        )
    ])

    # Update the layout
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 5]
            )),
        title=title
    )

    return fig

def main():
    st.title("Team Health Assessment")
    
    name = st.text_input('First name', '---')

    # Dictionary to store the ratings
    ratings = {}

    # Create sliders for each attribute
    for attribute, description in attributes_with_descriptions.items():
        st.markdown(f"### {attribute}")
        st.markdown(description)  # Display the description of each attribute
        # Use attribute as a unique key for the slider
        ratings[attribute] = st.slider("Rate this attribute", 0, 5, 0, key=attribute)

    # Show results button
    if st.button("Show Results"):
        # Data preparation
        values = [ratings[attr] for attr in attributes_with_descriptions.keys()]
        chart = make_spider_chart(values, list(attributes_with_descriptions.keys()), f"{name}'s Team Health Radar Chart ")
        
        # Display the radar chart using Plotly
        st.plotly_chart(chart)

if __name__ == "__main__":
    main()

