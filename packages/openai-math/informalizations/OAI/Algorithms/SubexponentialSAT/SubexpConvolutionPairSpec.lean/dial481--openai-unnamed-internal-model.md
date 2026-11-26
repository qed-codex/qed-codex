---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpConvolutionPairSpec.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpConvolutionPairSpec.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpConvolutionPairSpec.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Concrete instantiation of the convolution controller's local pair
contract. The base contains only static arithmetic data and empty work space;
the eleven controller buffers may vary on every invocation. 

### `pairSpec`

 Every varying controller buffer receives the same actual fixed pair
program. The only side condition on the base is its concrete static layout. 
