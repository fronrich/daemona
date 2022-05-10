# Data Breakdown

All interactions in this program will follow the same basic schema:

```jsonc
{
  // the part before the colon indicates the speaker
  // Daemona (D) or Host (H)
  // first part after the colon of id asserts whether this is a 
  // question (Q) or response (R)
  // This is based on who is currently speaking
  // If daemona asks the question, she is speaking
  // second part asserts tone, neutral (N), hostile (H), and imperative (I)
  // second part mainly affects responses, but helps set tone of questions
  // N leads to more questions
  // H leads to unintended actions
  // I makes daemona act upon a task
  // third part is an integer id for the index of the question/response
  // in its category
  "id": "X:X-X-X",
  // potential iterations of the same question
  "iterations": ["", "", ""],

  // mood indicator
  "sentiment": "mood_enum",


  // paths form conversation AI, and can either lead to actions or more questions
  // Q has responses, wherewas R has questions
  "paths": ["X:X-X-X", "X:X-X-X", "X:X-X-X"],

  // occasionally responses chosen will have events
  // associated with them
  // events are triggered when responses are chosen or said by daemona
  "events": ["event_enums"]
}
```
