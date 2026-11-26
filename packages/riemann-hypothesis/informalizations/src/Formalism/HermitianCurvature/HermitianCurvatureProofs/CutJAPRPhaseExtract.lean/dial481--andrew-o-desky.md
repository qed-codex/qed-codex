---
{
  "module": "src/Formalism/HermitianCurvature/HermitianCurvatureProofs/CutJAPRPhaseExtract.lean",
  "declarations": [
    "Formalism.FourierDecayAlt.P.CutMP.JA.SSn.Rep.Core.TC.PR.phase_extraction_holds"
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

## A radial polynomial representation outside a disc

[Theorem ALG.1104](https://andrewodesky.com/rh/lean/Formalism.FourierDecayAlt.P.CutMP.JA.SSn.Rep.Core.TC.PR.phase_extraction_holds/)

Let $T>0$ and $f:\mathbb C\to\mathbb C$. Suppose there are $m\ge0$ and $P\in\mathbb C[X,Y,Z]$ such that $$(|z|^2-T)^m f(z)=P\bigl(z,\bar z,\sqrt{|z|^2-T}\bigr)\qquad(|z|^2>T).$$ Assume $f(e^{i\theta}z)=f(z)$ for every real $\theta$ and every $|z|^2>T$. There are $n\ge0$ and $q\in\mathbb C[U]$ such that $$(|z|^2-T)^n f(z)=q\bigl(\sqrt{|z|^2-T}\bigr)\qquad(|z|^2>T).$$
