# FAQ and scenarios

## Scenarios
These scenarios may help with thinking through how you might approach fairness questions, and consider what may be similar or different in your problem context.  These scenarios do not include any specific guidelines and recommendations.


<div class="Scenario">
  <h4>Identifying potential tax fraud</h4>
  <p>You're a member of an analytics team in a European country, and brought in to consult about a project that has already started to scale the deployment of models for predicting which tax returns may require further investigation for fraud.  The team has used a model trained in other jurisdictions by a large predictive analytics supplier, and hopes that they can leverage this at a lower cost that would be required to invest in the capability in-house.
  </p>
  <a href="https://arxiv.org/pdf/1802.01029.pdf">Veale et al. (2018)</a>
</div>

<div class="Scenario">
  <h4>Measuring brand sentiment</h4>
  <p>You're a member of a team trying to measure brand sentiment from online comments and reviews.  The team hopes to use an existing language model, a third-party service for flagging abusive comments, and then train a more targeted sentiment classifier for your brand on top.
  </p>
  <a href="https://arxiv.org/pdf/2005.00813.pdf">Hutchinson et al. (2020)</a>
</div>

<div class="Scenario">
  <h4>Employment evaluations</h4>
  <p>A potential client asks you if ML can help with predicting job candidates' suitability for jobs based on a combination of personality tests and body language during recorded interview sessions.</p>
  <a href="https://arxiv.org/pdf/1906.09208.pdf">Rhagavan et al. (2019)</a>
</div>

<div class="Scenario">
  <h4>Rankings for image search</h4>
  <p>
    You're on a team working on improving an image search system after receiving some complaints from users related to fairness.  Users often use this system to find a selection of stock images to use when making multimedia presentations.  In this system, requests start with some information about the context and user creating the query, and your team is trying to incorporate ideas about fairness like diversity and inclusision into how search results are ranked.
  </p>
  <a href="https://arxiv.org/pdf/2002.03256.pdf">Mitchell et al. (2020)</a>
</div>

<div class="Scenario">
  <h4>Sales leads for car loans</h4>
  <p>You work at CarCorp, a company that collects special financing data: information on people who need car financing but have either low credit scores or limited credit histories, and sells this data to auto dealer as sales leads.  CarCorp  serves dealers across the United States.  A new project manager asks about leveraging data science to “improve the quality” of leads so that dealers to not churn.  CarCorp has a large amount of historical lead data (2 million leads in 2017 alone), but relatively less data on which leads had been approved for special financing (let alone why the loan was approved).
  </p>
  <a href="https://arxiv.org/ftp/arxiv/papers/1901/1901.02547.pdf">Passi and Barocas (2019)</a>
</div>

<div class="Scenario">
  <h4>Predictive policing</h4>
  <p>You are a contractor working with the police department in a large city.  One of the project leaders in the department would like to construct a risk score for people who are known gang members engaging in knife crime.  It's important to them that they can understand what the model is doing, and are way that any model will pick up on protected characteristics.
  </p>
  <a href="https://arxiv.org/pdf/1802.01029.pdf">Veale et al. (2018)</a>
</div>

<div class="Scenario">
  <h4>Scheduling maintenance within a factory</h4>
  <p>You work within a manufacturing company, and are starting a new project that will create a schedule assigning employees to check and update certain components of the machinery to prevent critical operation failures. The component assignment is based on data that show how often different components have worn out and broken down in the past.
  </p>
  <a href="https://ischool.utexas.edu/~ml48959/materials/Publication/2018-AlgoManagePerception.pdf">Kyung Lee (2018)</a>
</div>

<div class="Scenario">
  <h4>Child protective services hotline</h4>
  <p>You're collaborating with the child protective services agency as part of a county government in the US.  The agency is redesigning the intake flow for reports of potential child abuse or neglect, and wants to discuss if a predictive analytics system could help them improve this system.
  </p>
  <a href="https://www.andrew.cmu.edu/user/achoulde/files/accountability_final_balanced.pdf">Brown et al. (2019)</a> and <a href="http://proceedings.mlr.press/v81/chouldechova18a/chouldechova18a.pdf">Chouldechova et al. (2018)</a>
</div>

<style>
    .Scenario {
      margin-bottom: 20px;
      font-size: 12px;
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 10px;
      width: 300px;
      display: inline-block;
    }

    /* see https://www.w3schools.com/howto/howto_css_flip_card.asp */
     /* The flip card container - set the width and height to whatever you want. We have added the border property to demonstrate that the flip itself goes out of the box on hover (remove perspective if you don't want the 3D effect */
    .flip-card {
      background-color: transparent;
      width: 300px;
      height: 200px;
    }

    /* This container is needed to position the front and back side */
    .flip-card-inner {
      position: relative;
      width: 100%;
      height: 100%;
      text-align: left;
      transition: transform 400ms;
      transform-style: preserve-3d;
    }

    /* Do an horizontal flip when you move the mouse over the flip box container */
    .flip-card:hover .flip-card-inner {
      transform: rotateY(180deg);
    }

    /* Position the front and back side */
    .flip-card-front, .flip-card-back {
      cursor: default;
      border: 1px solid #ccc;
      border-radius: 10px;
      overflow-y: scroll;
      position: absolute;
      width: 100%;
      height: 100%;
      -webkit-backface-visibility: hidden; /* Safari */
      backface-visibility: hidden;
    }

    /* Style the front side (fallback if image is missing) */
    .flip-card-front {
      background-color: white;
      color: black;
      padding: 20px;
    }

    /* Style the back side */
    .flip-card-back {
      padding: 20px;
      background-color: #f8f8f8;
      color: #333;
      transform: rotateY(180deg);
    } 
  </style>