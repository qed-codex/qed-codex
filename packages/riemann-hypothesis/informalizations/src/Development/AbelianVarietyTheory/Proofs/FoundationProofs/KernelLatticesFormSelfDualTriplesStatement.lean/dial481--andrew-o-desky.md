---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/KernelLatticesFormSelfDualTriplesStatement.lean",
  "declarations": [
    "GlobalTheory.T.kernelLattices_form_selfDual_triples"
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

## Eighth roots of unity in compositions of theta intertwiners

[Theorem THETA.1483](https://andrewodesky.com/rh/lean/GlobalTheory.T.kernelLattices_form_selfDual_triples/)

Fix the full arithmetic datum specified in ([The convergent doubling integral identity](https://andrewodesky.com/rh/lean/GlobalTheory.T.doubling_basicIdentity_unfolding/)) with imaginary quadratic field $K=\mathbb Q(\sqrt{-d})$, its CM field and CM type. Let $\mathfrak c\ne0$ be an ideal of $\mathcal O_K$ with norm coprime to $2d$, and let $\delta^{12}$ equal the discriminant of its complex ideal lattice. Let $T$ be the elliptic lattice obtained by scaling that ideal lattice by $\delta$, and let $V$ be the complex matrix space with $N'\times N$ entries at each CM-type embedding, where $N,N'\ge0$. Put $$H(z,w)=\frac{\sum_{\tau,i,j}z_{\tau ij}\overline{w_{\tau ij}}}{\operatorname{area}(T)},\quad \alpha(x)=(-1)^{\operatorname{round}((\sqrt d/2)\operatorname{Re}H(x,x))},$$ $$U_xf(z)=f(z+x)e^{-\pi H(z,x)-\pi H(x,x)/2},\qquad b(x,y)=e^{-\pi i(\sqrt d\operatorname{Re}H(x,y)+\operatorname{Im}H(x,y))}.$$ Let $\Theta(A)$ consist of entire $f$ with $\alpha(x)U_xf=f$ for all $x\in A$. Allow lattices $A$ of either prescribed type: the elliptic lattice times an orthonormal matrix basis over $K$, or those constructed from a pair of self-dual Hermitian lattices.

Every allowed $A$ satisfies $W_xf=\alpha(x)U_xf$ for $x\in A$ and arbitrary $f$, where $W_x=e^{\pi i(\sqrt d/2)\operatorname{Re}H(x,x)}U_x$; also $b(x,y)=1$ for $x,y\in A$, and $b(x,y)=b(y,x)$ for all $y\in A$ implies $x\in A$. If $0\ne f\in\Theta(A_1)$ and $A_2$ is allowed, $[A_2:A_1\cap A_2]$ is finite. Define $$I_{12}f=[A_2:A_1\cap A_2]^{-1/2}\sum_{q\in A_2/(A_1\cap A_2)}\alpha(q)U_qf$$ with the prescribed representatives. Then $I_{11}f=f$ for every $f\in\Theta(A_1)$, and for allowed $A_1,A_2,A_3$ and $0\ne f\in\Theta(A_1)$ all three pair indices are finite and there exists $\mu\in\mathbb C$ such that $$\mu^8=1,\qquad I_{23}I_{12}f=\mu I_{13}f.$$
