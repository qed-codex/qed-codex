---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/MetaplecticCoverWeilRepresentationStatement.lean",
  "declarations": [
    "GlobalTheory.T.metaplectic_cover_weil_representation"
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

## Real metaplectic representation and Gaussian transform

[Theorem REP.1695](https://andrewodesky.com/rh/lean/GlobalTheory.T.metaplectic_cover_weil_representation/)

For every finite index set of cardinality $n$, there is a topological group $\widetilde G$ and a surjective covering homomorphism $p:\widetilde G\to\operatorname{Sp}_{2n}(\mathbb R)$ with kernel $\{1,\epsilon\}$, $\epsilon\ne1$. There are a unitary representation $\omega$ on $L^2(\mathbb R^n)$ and a representation $\omega_{\mathcal S}$ by continuous complex-linear operators on $\mathcal S(\mathbb R^n)$ such that $\omega(\epsilon)=-1$, every orbit map in $L^2$ is continuous, the action on $\widetilde G\times\mathcal S$ is jointly continuous, and $\omega$ agrees with $\omega_{\mathcal S}$ under the inclusion into $L^2$.

For $w=(a,b)\in\mathbb R^n\oplus\mathbb R^n$, define $$(\rho(w)f)(x)=e^{\pi i(2b\cdot x+a\cdot b)}f(x+a).$$ Then $\omega(g)\rho(w)=\rho(p(g)w)\omega(g)$. Write $p(g)=\begin{pmatrix}A&B\\C&D\end{pmatrix}$, $P=A-iB$, $Q=C-iD$, and $\phi(x)=e^{-\pi|x|^2}$. For each $g$ there is $c\in\mathbb C$ such that $$c^2\det P=1,\qquad (\omega_{\mathcal S}(g)\phi)(x)=c\exp\!\bigl(\pi i\,x^t(-QP^{-1})x\bigr).$$
