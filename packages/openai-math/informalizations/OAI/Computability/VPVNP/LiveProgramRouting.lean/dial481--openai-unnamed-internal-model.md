---
{
  "module": "OAI/Computability/VPVNP/LiveProgramRouting.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramRouting.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramRouting.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native path factorization at the three header decisions

A router contributes exactly one choice-free burst. Removing that burst is a
bijection from accepting paths to accepting continuations, with the report's
memory effect, returned cursor and contribution to the cost predicate retained.


### `Router`

 The three routing decisions, selecting the group mode, the incoming tail preparation, or
the outgoing tail preparation. 

### `stage`

 Stage at which the selected routing decision is executed. 

### `address`

 Geometry expression locating the header word that supplies this router's flag. 

### `target`

 Map a decoded flag ordinal to this router's acceptance, rejection, or stage-transfer
target. 

### `data`

 The router's two evaluated operands, the address of its decision flag and the address of
the outer stage tag. 

### `execute`

 At a checked flag this is the exact linked report, including rejection on
surplus choices and every external probe of the router and the outer dispatch. 

### `Continuations`

 The remaining calls use the precise memory and persistent word produced by
this deterministic burst. A terminal burst allows only the empty remainder. 

### `deterministicEquiv`

 A known successful choice-free first call is the unique first call on any
accepting path. This statement permits arbitrary clocks and report-dependent caps. 

### `Router.pathEquiv`

 Native path bijection at any of the live program's three decisions. 
