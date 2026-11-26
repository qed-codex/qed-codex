---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FlagMeasures/OffK0Closed.lean",
  "declarations": [
    "GlobalTheory.CarrierGap.offDiag"
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

## An off-diagonal bound for sums of geometric terms along a selection of spectral realizations

[Theorem THETA.1.1758](https://andrewodesky.com/rh/lean/GlobalTheory.CarrierGap.offDiag/)

Let $\mathcal C$ be a class of families and let $\sigma$ be a selection of spectral realizations on $\mathcal C$, with thresholds $x_\sigma(\mathrm{Fm})$, in the sense of ([Selections of spectral realizations, sums of geometric terms and two row hypotheses](https://andrewodesky.com/rh/lean/Formalism.L2.SG.ThmSOwn.SSelF/)). Assume the following.

1. The Siegel–Weil formula for the unitary groups of automorphic settings: item (1) of ([Three inputs for the selected off-diagonal bound](https://andrewodesky.com/rh/lean/PI.VolStabS.MassDataS.SWXS/)).
2. Hypothesis (non-generic row bound) of ([Selections of spectral realizations, sums of geometric terms and two row hypotheses](https://andrewodesky.com/rh/lean/Formalism.L2.SG.ThmSOwn.SSelF/)).
3. ([Hypothesis: the range of a product of a finite-adelic and a discrete-series convolution operator on a unitary group is finite-dimensional](https://andrewodesky.com/rh/lean/Formalism.L2.SG.RowsDef.RowsFinDim/)).
4. For every family $\mathrm{Fm}$ in $\mathcal C$ and every member $(x,i)$ of $\mathrm{Fm}$ with $x>x_1$ and $x\ge x_\sigma(\mathrm{Fm})$, the local comparison holds for the datum $D(x,i)$: item (2) of ([Three inputs for the selected off-diagonal bound](https://andrewodesky.com/rh/lean/PI.VolStabS.MassDataS.SWXS/)).
5. The lattice mass identities hold along $\mathcal C$ with constant $3$: item (3) of ([Three inputs for the selected off-diagonal bound](https://andrewodesky.com/rh/lean/PI.VolStabS.MassDataS.SWXS/)).
6. Hypothesis (row bounds for pairs of terms along a selection) of ([Selections of spectral realizations, sums of geometric terms and two row hypotheses](https://andrewodesky.com/rh/lean/Formalism.L2.SG.ThmSOwn.SSelF/)) holds for $\mathcal C$ and $\sigma$ with constant $3$.

Then the following holds for all sufficiently constrained families $\mathrm{Fm}$ of $\mathcal C$. There is $x_0$ such that at every member $(x,i)$ of $\mathrm{Fm}$ with $x\ge x_0$, $x>x_1$ and $x\ge x_\sigma(\mathrm{Fm})$ at which the family standing conditions with constant $3$ hold, every two distinct source words $u\ne u'$ of the datum $D(x,i)$ satisfy $$\bigl\|K^0_{u,u'}\bigr\|_{\rm HS}^{2}\ \le\ \bigl(1+b^{-6}\bigr)\,\frac{d_u\,d_{u'}}{D_*}.$$ Here $K^0_{u,u'}=K^0_{u,u'}(X,Y)$ is the sum of term operators over the identity, generic and non-generic terms for $(u,u')$, formed with the setting $X$ and the completion $Y$ of the selected realization $\sigma(x,i)$; $d_u$, $d_{u'}$ and $D_*$ are the dimensions and the real number of the datum $D(x,i)$; and $b=\exp(x^{\varepsilon})$ is formed from the size data of the member.
