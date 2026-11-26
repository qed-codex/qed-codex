---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/BatchDescent/Encoded.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/BatchDescent/Encoded.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/BatchDescent/Encoded.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Specialization of a sorting-based descent to exceptional widths 

### `Compilation`

 The compiler uses full-length sorting gates on ordinary records and
cheap short tables. Its cost counts every port, including those of sorts. 

### `descent`

 A single compiled graph yields both versions of the descent theorem
at the same length and with the same exponent. 

 # Recovering the lane and ordinal of each bundle from its short record 

 # A dictionary for the short per-host descriptions 

### `lookupSlot`

 Invert the local ordinal map. Outside a valid record the value
is immaterial; choose zero if no input bundle has this ordinal. 

 # Dyadic row and bin capacities for a batch recipe 

### `dimensions`

 One budget unit is one bit of the total incidence allowance. 

 # Reading the exterior decisions of all bins 

### `owner_location`

 Every active exterior row has an exterior channel and a
representative stack on that channel. 

### `Screen.observed`

 The common bin computation supplies both exterior checks. A long
name is needed only once per channel, regardless of the stack count. 


# Terminal metadata

Apart from the long names, one short descriptor per host determines
all the data used in its bin. Its decoder can be arbitrary. The
controller that produced these bits is accounted for by the stages.



# Quantitative interface for encoded beat sequences

Keep the exponent charged to long global names independent of the
terminal block reserve. The exponent charged to short records may
depend on the reserve. No payload passes through the control stages.


### `Encoded`

 Uniform controls for logarithmically many beats. 

 # Interpreting the short and long fields of terminal metadata 
