---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Assembly/Group/Model.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Assembly/Group/Model.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Assembly/Group/Model.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Locality of dyadic marks 

### `Walk`

 The index records the accumulated change of depth. 

### `Window`

 Slots may repeat a host. Edges that can only act above the height
budget need not be stored. 

 # Bounded records for local grouping decisions 

### `Patch`

 Live bit, the two neighbor masks, then loads of all group members
at the visible hosts. Position zero is the center. 

### `Summary`

 Split counts and all candidate labelings. 


# Electing the common mixer and recovering dyadic leaf labels

Only local load and incidence records index the table of candidates.
The common mixer is elected by summing the split counts over live hosts.



# Uniform grouping network

There are two table labels. Their arities are independent of the number
of hosts and the number of groups. The only long-range operation is
the election on columns of short split counts.


 # The computed labels certify a balanced partition 


# Names and neighbors of child hosts

An address consists of a parent host and a dyadic interval. Only
intersecting intervals at nearby depths need neighbor slots. Their
enumeration is fixed by the height and degree, independently of the
parent graph. A third neighborhood gives the post-contraction graph.


 # Exact support of the child host dictionary 

 # The grouping record at a host and group index 

 # Interpreting the live rows of a grouping controller 

### `Presents`

 The two masks distinguish graph edges and core edges from padding.
The address of every neighbor of a live host is itself live. 

 # Computing the child contact lists 

### `step_depends`

 The seat of a candidate is fixed by the output index. Each output
bit reads an activity flag and at most one parent-address bit. 

### `cheap`

 Construct the one-step graph and then enumerate the third neighborhood. 
