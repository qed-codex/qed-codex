---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/AbsSubOfDisjoint.lean",
  "declarations": [
    "GlobalTheory.JointHarm.joint_harmonics"
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

## Highest-weight multiplicities in joint harmonics

[Theorem THETA.1180](https://andrewodesky.com/rh/lean/GlobalTheory.JointHarm.joint_harmonics/)

Let $p,q,r,s\ge0$, let $I=I_+\sqcup I_-$ have block sizes $p,q$, and let $J=J_+\sqcup J_-$ have block sizes $r,s$. On $\mathcal P=\mathbb C[z_{ac}:(a,c)\in I\times J]$, set $L_{ac}=\partial_{ac},R_{ac}=z_{ac}$ for matching block signs and $L_{ac}=z_{ac},R_{ac}=-\partial_{ac}$ otherwise. Define complex-linear matrix actions by $$D_1(E_{ab})=\sum_{c\in J}(R_{ac}L_{bc}+\tfrac12\delta_{ab}),\qquad D_2(E_{ce})=\sum_{a\in I}(R_{ac}L_{ae}+\tfrac12\delta_{ce}).$$ Let $\mathcal H$ be the common kernel of the degree-lowering-by-two parts of $D_1(Z)$ and $D_2(Z')$ for all $Z,Z'$ with zero diagonal blocks. For rational weights $\mu\in\mathbb Q^I$, $\mu'\in\mathbb Q^J$, let $\mathcal H_{\mu,\mu'}$ be the subspace of $\mathcal H$ on which diagonal matrix units act with weights $\mu,\mu'$, and strictly upper matrix units within each block of either action act by zero.

Set $\widehat\mu=(\mu|_{I_+}-(r-s)/2,\ \mu|_{I_-}+(r-s)/2)$ and $\widehat\mu'=(\mu'|_{J_+}-(p-q)/2,\ \mu'|_{J_-}+(p-q)/2)$. The dimension of $\mathcal H_{\mu,\mu'}$ is one precisely when there are weakly decreasing integer lists $a,b,c,d$, with $a,c$ strictly positive entrywise and $b,d$ strictly negative entrywise, such that $$\begin{aligned} \ell(a)+\ell(b)&\le p,&\ell(c)+\ell(d)&\le q,\\ \ell(a)+\ell(d)&\le r,&\ell(c)+\ell(b)&\le s, \end{aligned}$$ $$\widehat\mu=(a,0^{p-\ell(a)-\ell(b)},b\ ;\ c,0^{q-\ell(c)-\ell(d)},d),$$ $$\widehat\mu'=(a,0^{r-\ell(a)-\ell(d)},d\ ;\ c,0^{s-\ell(c)-\ell(b)},b).$$ If no such lists exist, $\mathcal H_{\mu,\mu'}=0$. Here $\ell$ is list length, $0^k$ is a list of $k$ zeros, commas concatenate lists, and the semicolon separates the two blocks.
