---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafRingSetupProgramPorts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafRingSetupProgramPorts.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafRingSetupProgramPorts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed physical layout for native ring preparation.

The local setup has 32 registers and 640 stacks.  It can be lifted into the
40-register/768-stack leaf caller.  The collector's stacks 320--339 are never
used.  Arithmetic metadata is written directly to its native consumer port;
temporary search, scalar, table, and node data have disjoint workspaces.


### `parameters`

 The runtime numerical bank is kept until every unary serialization and
node-count copy has finished. 

### `search`

 Search depth is the final native ring dimension.  The encoded F3
coefficient list on 195 is temporary; padding consumes it. 

### `scalar`

 Boot, scalar-cache construction, and (when needed) Newton preparation
share this local workspace.  The binary-t input remains a private copy. 

### `table`

 Padded coefficients remain at search port21 =441.  Scalar one is copied
to the consumed seed538; its canonical master at498 is preserved. 

### `constant`

 Dynamic-d constant vectors have separate scratch from table generation.
Only their output location varies among full one, minus one, and zero. 

### `search_avoids_collector`

 These are preservation statements about physical ports, independent of
all runtime values and dimensions. 

### `idempotent`

 The closed idempotent program is run in a private workspace after the
ordinary ring setup. Its local cleanup therefore cannot clear native t or
other metadata. Repeating its scalar preparation has polynomial cost. 

### `wideRegisters`

 Leave the parser/branch registers16--23 untouched when this setup is
called inside the agreed 40-register leaf ambient. 
