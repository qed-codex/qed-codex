---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Assembly/Mixer/Choice.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Assembly/Mixer/Choice.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Assembly/Mixer/Choice.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading contact loads from local patterns

The neighbor list may repeat the host itself. Choose one column per
oriented core contact, using the occupied column whenever there are
demands. All other columns contribute zero to the mixer score.



# Position and contact rows for the reset

Flatten a host and a short column index. Reserve one column for
the load of the position and one per neighboring host for outgoing
demands. All duplicate and unused contact columns have zero load.


 # Correctness of load extraction from a posting 


# Computing base depths from the navigation masks

A port may repeat its own host address. Take the maximum of all
reported lower bounds. Missing tethers are harmless when their
delay exceeds the entire range of possible base depths.



# Exact summaries of a posted network

The counter and the pattern of a single occurrence determine its
scaled load and its unit counts by outgoing contact. The initial
base depth is read from the sum of these short load words.


 # Selecting a valid reset schedule from a template 

### `Fits`

 Number-format and graph bounds required by the reset controller. 
