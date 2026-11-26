---
{
  "module": "OAI/Computability/VPVNP/LiveStageLink.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveStageLink.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveStageLink.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Linking finite native burst-RAM stages

Each call reads a stage tag at a designated public address. It then runs the
selected finite instruction table with fresh private memory and the original
persistent word. A continuing return stays in that stage. An accepting exit
can finish the entire program or store the next stage tag and return zero for
its first call. The tables have distinct program-counter spaces and share their
ordinary register and public-word spaces. Three extra registers hold the tag
address, its value, and a comparison or transfer literal.


### `Label`

 Two startup instructions, a tag scan, relocated component code, and three
post-accept instructions per possible transfer. 

### `codeSize`

 Number of linked program counters for bootstrap, tag scan, tag comparisons, component
bodies, and three handoff positions per stage. 

### `labelEquiv`

 A concrete numbering for the linked program, independent of the runtime word width. 

### `boot`

 Linked program counter for one of the two bootstrap instructions. 

### `scan`

 Linked program counter for a tag-scan position, including the terminal scan position after
all stages. 

### `compareTag`

 Linked program counter for the tag comparison with the specified stage. 

### `bodyPC`

 Embed a stage-local instruction address in the linked program's disjoint component-body
region. 

### `handoff`

 Linked program counter for one of a stage's three handoff instructions. 

### `reg`

 Component register numbers occupy the low end of the common file. 

### `addrReg`

 First extra register after the component bank, holding the address of the outer tag cell. 

### `tagReg`

 Second extra register, holding the tag value read from external memory. 

### `tmpReg`

 Third extra register, used for the comparison or transfer literal. 

### `bodyInstr`

 Relocate each operand and jump target while preserving the ordinary
opcode. A transfer replaces only the accepting halt of its component. 

### `literalWidth`

 The literal width accommodates every component constant and every stage tag. 

### `tagWord`

 Encode a stage ordinal as a RAM word at the specified width. 

### `linked`

 Combine the stage tables and successor map into a native template with three extra
registers and one extra public tag-address operand. 

### `publicData`

 Extend the ordinary public words with the reserved external tag address. 

### `machine`

 Instantiate the linked template with the component public words and the tag-cell address. 
