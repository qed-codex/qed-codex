---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Routing/Algorithm/Computability.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Routing/Algorithm/Computability.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Routing/Algorithm/Computability.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Straight-line word programs with indexed loads

Data are single bits, bounded unsigned words, pairs, and dyadic
arrays. Pairs and arrays are immutable and can be shared by address.
A program is independent of its input. Tabulation writes a fresh
array in increasing index order, with the program for each index
included in the instruction count. A literal, including a static
index, occupies one word. Boolean gates have four-bit truth tables.

The rules give the denotation and charge of a program simultaneously.
The width bounds apply to arithmetic operands and literals. To address
storage one may take the maximum of this width and the binary length
of the input and the allocated words. There is no unit-cost primitive
for evaluating large tables, searching, or sorting.


 # Bounds for near-linear word programs 

 # Extracting deterministic code and a bound on its advice and working memory 

### `advice_scratch`

 The time allowance covers both the program words and the scratch
allocation, including the extra words of all tabulations. 

### `RAM.code`

 One fixed program handles every input. Its time, static advice and
scratch allocation are linear in the original charge. 

 # Counting active dummy edges by colour

The scan can be unrolled before the input is known. A counter has
h+1 bits, so even a count of all 2^h indices fits without overflow.


 # Controller operations on tables of addresses 

### `Computability`

 The cost bounds are independent of the height and the fixed tables.
The inverse need only be correct on permutations. 


# Compiling local observations

The list of group elements and the table on their coincidences are
fixed before the height or the permutation is given.



# Compiling local functions of marked sites

The permutation determines the addresses. Compare them and gather the
marks there before applying the fixed local table.



# Dispatching to an action chosen at each site

A local decision names a member of a fixed list of actions. To
materialize one address bit the circuit needs only the encoded decision
and the corresponding bit of each candidate address.



# A fixed decision table for a local action program

The input to this table contains only equality bits and selector marks.
Its shape is independent of the height. Compile by exhaustive tests
against its finitely many possible inputs, charging for every test.

