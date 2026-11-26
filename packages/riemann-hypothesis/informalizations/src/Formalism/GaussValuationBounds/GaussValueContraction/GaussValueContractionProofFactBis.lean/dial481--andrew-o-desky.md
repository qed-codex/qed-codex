---
{
  "module": "src/Formalism/GaussValuationBounds/GaussValueContraction/GaussValueContractionProofFactBis.lean",
  "declarations": [
    "Formalism.NOK.cjExist_proof"
  ],
  "author": "dial481",
  "writer": "Andrew O'Desky",
  "origin": "other-author",
  "source": "https://andrewodesky.com/rh/",
  "source_commit": "40e56bab026552e089d7afcfeff08d2defb9c005",
  "license": "with-permission"
}
---

As published on 26 November 2026.

## Valuations of differences of normalized character powers

[Theorem PHT.0660](https://andrewodesky.com/rh/lean/Formalism.NOK.cjExist_proof/)

Let $\ell$ be an odd prime and let $\chi\in\mathbb Z_\ell^\times$ satisfy $v_\ell(\chi-1)=1$. There is a function $c:\mathbb Z\to\mathbb Z_\ell$ such that $$-\ell c_j=\chi^{-j}-1,\qquad c_0=0.$$ For distinct integers $j,j'$, $$c_j-c_{j'}\ne0,\qquad v_\ell(c_j-c_{j'})=v_\ell(j-j').$$
