---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapRowCode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapRowCode.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapRowCode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite instruction table for one decoded base row

The field setup and padded reader have four and seven instruction rows per
endpoint. Their exits follow the fixed field order. The lookup and offset
advance blocks use their own finite labels. A pair of final instructions
returns the parameter ordinal or rejects.


### `Address`

 Distinct addresses of all instruction rows, including the two exits. 

### `fieldSites`

 Program counters for the four setup instructions and seven padded-reader instructions of
each endpoint, relocated into the row's address space. 

### `lookupPC`

 Relocate a label of the matrix lookup flow to its instruction address in the row table. 

### `advancePC`

 Relocate a label of the group offset advance flow to its instruction address in the row
table. 

### `exitPC`

 The row's normal return address when `bad` is false or its rejecting address when `bad` is
true. 

### `afterField`

 Resolve the fall-through after the field's reader against the fixed field order. 

### `text`

 Instructions for the fixed base row in a larger enclosing instruction address space. 

### `inBody`

 The normal and rejecting exits can instead belong to the enclosing evaluator. 

### `linked`

 Linking the concrete text supplies the instruction hypotheses of each subroutine. 

### `addresses`

 Numerical labels chosen entirely from the finite table, before word width or input. 

### `template`

 A standalone executable template whose normal exit returns the emitted ordinal. 

### `template_text`

 The standalone table has all required instruction rows for every word width. 

### `RowAddress`

 All counters of a decoded base row's code. 

### `rowSites`

 Link a row's fixed setup, read, lookup and cursor advance to the chosen PC positions. 

### `row_linked`

 Only the indicated body addresses are required to match. The exit addresses
can hold the next iteration or the caller's rejection instruction. 

### `row_template`

 A single finite machine text realizes the decoded row links simultaneously for all
word widths and public inputs. Its size uses only the fixed motif data. 

### `Port`

 Width constants, every compared row word, and every emitted ordinal can occupy
separate public ports of the fixed program. 

### `publicWords`

 Public-word assignment for one selector, grid point, and party, giving the group widths,
the expected digit at each row field, and the parameter ordinal of each matched row. 
