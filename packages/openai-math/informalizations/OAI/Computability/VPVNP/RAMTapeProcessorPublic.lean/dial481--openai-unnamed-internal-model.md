---
{
  "module": "OAI/Computability/VPVNP/RAMTapeProcessorPublic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeProcessorPublic.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeProcessorPublic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Public registers of the fixed site processor

The fields produced by the physical reader share a bank with the cost endpoints
and three instruction tallies. All routines use four temporary stacks in common.
Their finite tables depend only on the processor's fixed parameters.


### `Extra`

 Additional processor registers for fuel, credits, choice bounds, costs, initial-record
words, and four scratch stacks. 

### `Port`

 Combined site-setup ports and the additional public processor registers. 

### `rawPort`

 Input stack carrying the physical site tape before parsing. 

### `fuelPort`

 Unary per-call private instruction allowance. 

### `creditPort`

 Unary call credits prepared from the site’s bucket capacity. 

### `budgetPort`

 Unary upper bound on the length of the site’s private choice string. 

### `capPort`

 Word encoding the global cumulative-cost cap. 

### `startPort`

 Word encoding the beginning of the site’s cost interval. 

### `endPort`

 Word encoding the end of the site’s cost interval. 

### `initPort`

 Word holding the validator’s fixed initial-state literal. 

### `addressWordPort`

 Padded word containing the site address for the initial record. 

### `headerWordPort`

 Padded word containing the four header bits for the initial record. 

### `widthPort`

 Unary width of each word in the physical RAM records. 

### `lengthPort`

 Retained unary length of the original input tape. 

### `addressWidthPort`

 Retained unary address width of the site. 

### `bucketPort`

 Retained unary capacity of a site’s cost bucket. 

### `addressPort`

 Stack carrying the parsed site-address bits. 

### `headerPort`

 Stack carrying the four parsed header bits. 

### `incidentPort`

 Stack carrying the parsed incident vector. 

### `bucketLogPort`

 Stack holding the binary logarithm of the power-of-two bucket capacity in unary. 

### `result`

 Public bank after fuel, credits, choice budget, global cap, site endpoints, and the fixed
initial word have been prepared. 

### `parameters`

 Prepare the fuel and choice tallies, global cap, site cost endpoints, and fixed
initial-state word in that order. 

### `steps`

 Sum of the step counts for fuel preparation, the global cap, endpoint words, and the
initial literal. 

### `capFits`

 The fixed register table derives its cost width from the length. 

### `rawResult`

 Site-setup bank for the parsed program prefix, address, header, and incident vector with
word and sorting sizes prepared. 

### `startup`

 Parse and size the physical site, then initialize the public execution parameters. 

### `clockCoefficient`

 Fixed coefficient bounding the work of parsing, sizing, and initializing the public
processor bank. 

### `startup_runs`

 Run the actual parser and cost register table from the sole original input stack. 
