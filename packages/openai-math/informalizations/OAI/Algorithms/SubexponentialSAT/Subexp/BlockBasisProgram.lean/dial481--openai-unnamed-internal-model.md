---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/BlockBasisProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/BlockBasisProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/BlockBasisProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Copying the actual searched local basis/complement table

This module identifies the input and output of the fixed block-copy program
with the concrete arrays returned by the local finite search.  Its measured
execution begins with the encoded local table already present.  It does not
assign unit cost to constructing or encoding that table.


### `candidateEntries`

 Explicit vector-major, coordinate-minor order for a candidate tuple. 

### `pairEntries`

 The kernel tuple is followed by the complementary tuple. Their lengths
remain separate input metadata; no delimiter is inserted among field entries. 

### `dimensions_add`

 Independence and spanning of the searched pair determine the number of
stored vectors; this is derived from its actual correctness proof. 

### `blockEntries`

 The semantic array is repeated once per block, in the same order as the
fixed program's repeated bitstring. 

### `pair_program_trace`

 Actual fixed-instruction execution on a correct local basis/complement
table. The local table is preserved and the exact block table is output. 

### `searchedPair_program_trace`

 Specialization to the exact tuple returned by the finite local search;
no independently supplied basis or dimension hypothesis is needed. 

### `searchedPair_program_primitive`

 The same specialization in the actual compiled binary-machine semantics. 

### `searchedPair_trace_bound`

 Polynomial global cost for copying the exact searched table. The block
search and field-code width are visible local parameters. 

### `blockCount_le`

 A nonempty packed block supplies an injection from block indices into the
global coordinates, so the global factor in the runtime is derived from the
actual packing. 

### `searchedPair_packing_primitive`

 The copied, searched basis table has a real binary-machine run with a
bound polynomial in the number of global coordinates. The only local size
in the bound is the proved `N² * code.width` table length. 
