---
{
  "module": "src/CompanionTheory/SpectralGeometry/LocalGlobalProofs/StableLattices/ExistsUniformizerNonarchimedeanStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_uniformizer_nonarchimedean"
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

## A uniformizer in a proper ultrametric normed field

[Theorem ALG.1507](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_uniformizer_nonarchimedean/)

Let $L$ be a nontrivially normed field whose norm is ultrametric and whose closed bounded subsets are compact. There is $\pi\in L^\times$ such that $$\|\pi\|<1,\qquad \forall x\in L^\times\ \exists a\in\mathbb Z:\ \|x\|=\|\pi\|^a.$$
