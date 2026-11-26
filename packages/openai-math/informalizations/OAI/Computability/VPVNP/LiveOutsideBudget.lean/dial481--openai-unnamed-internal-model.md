---
{
  "module": "OAI/Computability/VPVNP/LiveOutsideBudget.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveOutsideBudget.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveOutsideBudget.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Choosing the physical processor count after the live preparation costs

The bound covers the header, preparation of the auxiliary inputs, the
exponent check and the evaluator tail. It bounds the tail uniformly over
all actual advice prefixes of the reserved size. The majorant substitutes
the input length for the RAM word width. For every fixed address exponent
this substitution holds eventually, so the polynomial degree in the
majorant is selected before that address exponent.


### `tailMajorant`

 A polynomial expression dominating either tail route at any raw prefix
length up to `A` and word width up to `W`. 

### `tail_polynomial`

 Polynomially bounded components remain polynomially bounded under the
tail majorant, without a common degree assumption on their five functions. 

### `dimensions`

 Raw dimensions, independent of the address exponent. 

### `upperHeader`

 Evaluate the header dimensions at the bounding geometry for input length n to estimate the
outside-stage work. 

### `auxWords`

 Maximum number of populated words of the auxiliary header. It excludes
both unused tails of the two exterior buffers. 

### `majorant`

 Header checks and all non-compression phases of a single live group.
Both route costs may be added when taking the common bound. 

### `actualBound`

 The group budget in the actual word geometry, with its true advice prefix
length and actual selected tail route. Compression is accounted separately. 

### `eventually_budget`

 The choice of B precedes the eventual threshold and applies uniformly
to the physical word widths and all bounded group inputs. 

### `eventually_actual`

 One eventual threshold works for every physical group, every eligible
advice string and every choice of the tail route. 
