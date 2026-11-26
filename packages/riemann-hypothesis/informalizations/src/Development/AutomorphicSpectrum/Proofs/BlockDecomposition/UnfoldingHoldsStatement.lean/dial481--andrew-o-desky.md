---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/UnfoldingHoldsStatement.lean",
  "declarations": [
    "GlobalTheory.T.unfolding_holds"
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

## Unfolding a nondegenerate Fourier coefficient of a Siegel Eisenstein series

[Theorem THETA.1615](https://andrewodesky.com/rh/lean/GlobalTheory.T.unfolding_holds/)

Fix the global unitary datum in ([The convergent doubling integral identity](https://andrewodesky.com/rh/lean/GlobalTheory.T.doubling_basicIdentity_unfolding/)), giving a CM extension $E/F$ with its embeddings, and let $G=U(n,n)$, $P\subseteq G$ its Siegel parabolic, and $V$ a Hermitian space of dimension $m$. Assume $$n<m\le2n,\qquad n+\operatorname{WittIndex}(V)<m.$$ Choose the source's standard Weil–Schwartz package $(\psi,\chi,\omega,H,\Phi)$ and its Haar measure on $U(V)(\mathbb A_F)$. In particular $\psi$ is a continuous unitary nontrivial additive character of $\mathbb A_F/F$, $\chi$ has the prescribed restriction, $\omega$ is the Weil action for a covolume-one measure, $H$ is the chosen height, and $\Phi$ lies in the specified polynomial Fock space for the given real parameters and Cartan involutions. Write $f_s(g)$ for the associated Siegel section and $$E(g,s)=\sum_{\gamma\in(P(F)\cap G(F))\backslash G(F)}f_s(\gamma g).$$ Let $N(b)=\begin{pmatrix}1&b\\0&1\end{pmatrix}$ for $b\in\operatorname{Herm}_n(\mathbb A_F\otimes E)$, let $db$ and $\mathcal D$ be an additive Haar measure and a rational-lattice fundamental domain of volume one, and let $w=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$. For every nondegenerate $\beta\in\operatorname{Herm}_n(E)$, $\Re s>n/2$, and $g\in G(\mathbb A_F)$, the function $b\mapsto f_s(wN(b)g)$ is integrable and $$\int_{\mathcal D}E(N(b)g,s)\psi\!\left(-\tfrac12\operatorname{Tr}_{E/F}\operatorname{tr}(\beta b)\right)db=\int_{\operatorname{Herm}_n(\mathbb A_F\otimes E)}f_s(wN(b)g)\psi\!\left(-\tfrac12\operatorname{Tr}_{E/F}\operatorname{tr}(\beta b)\right)db.$$
