---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderScalarProtected.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderScalarProtected.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderScalarProtected.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Protected addresses in arbitrary scalar-stage calls

The structured program text tracks which registers contain addresses read
from designated public slots. Every external write of a scalar header stage
uses such a register. This remains true on malformed memory, regardless of
branch choices or fuel, so the outer dispatch tag below the scratch base is
preserved at every continuing call.


### `Marks`

 A Boolean mark per register identifying those tracked by the analysis of external write
addresses. 

### `line`

 A set register bit certifies that it holds an address different from the
protected cell. Arithmetic and external reads discard this information. 

### `analyze`

 Sequential code passes its output marks to the next instruction. A
branch retains exactly the marks common to its two exits. 

### `Valid`

 Every marked register's word address differs from the designated protected address. 

### `scalarStage`

 The widths, four boundary flags, first-tail flag, mode and eight
descriptors each write into statically designated scalar scratch cells. 
