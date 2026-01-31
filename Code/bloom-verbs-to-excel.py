from typing import Dict, List
import pandas as pd

RAW_TRIGGERS: Dict[str, List[str]] = {
    "Remember": ["Cite","Define","Describe","Draw","Enumerate","Identify","Index","Indicate","Label","List","Match","Meet","Name",
                 "Outline","Point","Quote","Read","Recall","Recite","Recognize","Record","Repeat","Reproduce","Review","Select",
                 "State","Study","Tabulate","Trace","Write"],
    "Understand": ["Add","Approximate","Articulate","Associate","Characterize","Clarify","Classify","Compare","Compute","Contrast",
                   "Convert","Defend","Describe","Detail","Differentiate","Discuss","Distinguish","Elaborate","Estimate","Example",
                   "Explain","Express","Extend","Extrapolate","Factor","Generalize","Give","Infer","Interact","Interpolate", "Interpret",
                   "Observe", "Paraphrase", "Picture graphically", "Predict", "Review", "Rewrite", "Subtract", "Summarize",
                   "Translate", "Visualize"],
    "Apply": ["Acquire","Adapt","Allocate","Alphabetize","Apply","Ascertain","Assign","Attain","Avoid","Back up","Calculate",
              "Capture","Change","Classify","Complete","Compute","Construct","Customize","Demonstrate","Depreciate","Derive",
              "Determine","Diminish","Discover","Draw","Employ","Examine","Exercise","Explore","Expose","Express", "Factor", "Figure",
             "Graph", "Handle", "Illustrate", "Interconvert", "Investigate","Manipulate","Modify", "Operate", "Personalize",
              "Plot","Practice", "Predict", "Prepare", "Price", "Process", "Produce", "Project", "Provide", "Relate", "Round off",
             "Sequence", "Show", "Simulate", "Sketch", "Solve", "Subscribe", "Tabulate", "Transcribe", "Translate", "Use"],
    "Analyze": ["Analyze","Audit","Blueprint","Breadboard","Break down","Characterize","Classify","Compare","Confirm","Contrast",
                "Correlate","Detect","Diagnose","Diagram","Differentiate","Discriminate","Dissect","Distinguish","Document",
                "Ensure","Examine","Explain","Explore","Figure out","File","Group","Identify","Illustrate","Infer","Interrupt",
                "Inventory", "Investigate", "Layout", "Manage", "Maximize", "Minimize", "Optimize", "Order", "Outline", "Point out",
                "Prioritize", "Proofread", "Query", "Relate", "Select", "Separate", "Subdivide", "Train", "Transform"],
    "Evaluate": ["Appraise","Assess","Compare","Conclude","Contrast","Counsel","Criticize","Critique","Defend","Determine",
                 "Discriminate","Estimate","Evaluate","Explain","Grade","Hire","Interpret","Judge","Justify","Measure","Predict",
                 "Prescribe","Rank","Rate","Recommend","Release","Select","Summarize","Support","Test","Validate","Verify"],
    "Create": ["Abstract","Animate","Arrange","Assemble","Budget","Categorize","Code","Combine","Compile","Compose","Construct",
               "Cope","Correspond","Create","Cultivate","Debug","Depict","Design","Develop","Devise","Dictate","Enhance",
               "Explain","Facilitate","Format","Formulate","Generalize","Generate","Handle","Import","Improve","Incorporate",
               "Integrate","Interface","Join","Lecture","Model","Modify","Network","Organize","Outline","Overhaul","Plan",
               "Portray","Prepare","Prescribe","Produce","Program","Rearrange","Reconstruct","Relate","Reorganize","Revise",
               "Rewrite","Specify","Summarize"]
}

# Convert dict to DataFrame (lists can be different lengths)
df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in RAW_TRIGGERS.items()]))

# Write to Excel
df.to_excel("bloom_verbs.xlsx", index=False)
