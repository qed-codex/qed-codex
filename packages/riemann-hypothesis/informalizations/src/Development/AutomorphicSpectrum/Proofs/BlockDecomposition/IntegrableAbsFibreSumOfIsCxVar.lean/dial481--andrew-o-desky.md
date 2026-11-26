---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/IntegrableAbsFibreSumOfIsCxVar.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.Ar.Pub.CxAbs.integrable_absFibreSum_of_isCxVar"
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

## Absolute integrability of logarithmic sheet densities

[Theorem ARAK.1719](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Ar.Pub.CxAbs.integrable_absFibreSum_of_isCxVar/)

Let $K$ be a nonempty finite set, $(I_k)_{k\in K}$ finite coordinate sets, and $Q\subseteq\mathbb C[x_{k,i}]$ a relevant multihomogeneous prime with $\dim\mathbb C[x]/Q=e+|K|$. Let $C_Q$ be its zero set with every coordinate block nonzero. Write $s(z)=(\prod_k z_{k,i_k})_{(i_k)}$ for the Segre coordinate vector. Let $\Psi:\mathbb C^{\prod_k I_k}\to\mathbb C^{e+1}$ be linear and assume $\Psi(s(z))\ne0$ for every $z\in C_Q$.

A smooth Hermitian multidegree $a\in\mathbb Z^K$ is represented by a positive smooth function $h$ on the nonzero-block locus with $$h((c_kz_{k,i})_{k,i})=\left(\prod_k|c_k|^{a_k}\right)h(z)\quad(c_k\ne0).$$ Choose $e$ such metrics $h_1,\ldots,h_e$ of arbitrary integer multidegrees, and a further metric $h_A$ of multidegree $a\in\mathbb N^K$. Let $P\notin Q$ be a complex polynomial multihomogeneous of multidegree $a$, and put $g(z)=\log(|P(z)|/h_A(z))$, with the convention $\log0=0$.

For $y\in\mathbb C^e$, let $F_y=\{s(z):z\in C_Q,\ \Psi(s(z))=(1,y)\}$. For $w\in F_y$, choose a local holomorphic lift $\gamma$ through $w$ satisfying $\Psi(s(\gamma(t)))=(1,t)$. Let $D(y,w)$ be $g(\gamma(y))$ times the Lebesgue density at $y$ of $\bigwedge_{j=1}^e dd^c\log h_j(\gamma(t))$, where $dd^c=(i/\pi)\partial\bar\partial$; set it to zero if no such lift exists. Then $$y\longmapsto\sum_{w\in F_y}|D(y,w)|\quad\text{belongs to }L^1(\mathbb C^e).$$
