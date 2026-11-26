---
{
  "module": "src/Formalism/LocalToGlobal/KernelLattices/XiIndCClass.lean",
  "declarations": [
    "Formalism.L2.Ker.AC",
    "Formalism.L2.Ker.BC",
    "Formalism.L2.Ker.LamC",
    "Formalism.L2.Ker.thC",
    "Formalism.L2.Ker.xiL"
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

## Finite theta transforms of period lattices

[Definition / hypothesis THETA.D186](https://andrewodesky.com/rh/lean/Formalism.L2.Ker.thC/)

Construction (finite theta transform). Use ([Arithmetic field models for kernel comparisons](https://andrewodesky.com/rh/lean/Formalism.L2.Col.Fields/)), ([Decorated lattices and auxiliary kernel characters](https://andrewodesky.com/rh/lean/Formalism.L2.Col.Deco/)), and ([Fourfold theta kernels and lattice intertwiners](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.H.StdData/)). Write $E$ for the model field. Fix embeddings $e_\tau:E\hookrightarrow\mathbb C$, $\delta\in\mathbb C$, $d,c\in\mathbb N$, $h\in\mathbb R$, an integral module $A\subset E$, prime set $S$, and integral modules $N\subset E^a,N'\subset E^b$. Put $$M=\operatorname{span}_{\mathcal O_E}\{ux:u\in A,\ xN\subseteq N'\},\qquad \iota(x)=(\delta e_\tau(x_{ij}))_{\tau,i,j},\qquad L=\iota(M).$$ For a prime $P$ define $\varepsilon_P=1$ if $P\in S$, $\varepsilon_P=-1$ if $P\notin S,\bar P\in S$, and zero otherwise. Set $$M_- =\{x:c^{\varepsilon_P}x\in M_P\text{ for every }P\},\qquad M_+=\{x:c^{-\varepsilon_P}x\in M_P\text{ for every }P\},\quad L_-=\iota(M_-),\quad L_+=\iota(M_+).$$ On $V=\mathbb C^{\mathcal T\times\{0,\ldots,b-1\}\times\{0,\ldots,a-1\}}$, define $$H(z,w)=h\sum_{\tau,i,j}z_{\tau ij}\bar w_{\tau ij},\qquad\alpha(z)=\exp(\pi\mathrm i\sqrt d\operatorname{Re}H(z,z)/2),\qquad (U_xF)(z)=F(z+x)e^{-\pi H(z,x)-\pi H(x,x)/2}.$$

For additive subgroups $L_1,L_2$, fix a finite representative set $R(L_1,L_2)$ contained in $L_2$, with exactly one representative for every coset modulo $L_1\cap L_2$, whenever such a finite set exists. If none exists use a fixed arbitrary finite set. Put $$X=R(L,L_-),\qquad Y=R(L_+,L\cap L_-),\qquad Z=R(L,L_+).$$ For $\Xi:\operatorname{Hom}_E(E^a,E^b)\to\mathbb C$, define $\widetilde\Xi(v)$ by evaluating $\Xi$ at a fixed preimage of $v$ under $\iota$ when one exists and by zero otherwise. The finite theta transform of a function $e:V\to\mathbb C$ is $$\mathscr T_{N,N',S,c}(\Xi,e)=\sum_{x\in X}\alpha(x)U_x\left(\sum_{z\in Z}\frac{\alpha(z)}{|Y|}\left[\sum_{y\in Y}\widetilde\Xi(y-x)e^{2\pi\mathrm i\operatorname{Im}H(y,z)}\right]U_z e\right).$$ The reciprocal $|Y|^{-1}$ has value zero when $Y$ is empty. These definitions include their fixed choice conventions and do not assert that the representative sets or preimages exist in every case.

For later integrality conditions, a scalar is integral off a finite set $S_0$ of rational primes if it is algebraic and has absolute value at most one under every embedding $\overline{\mathbb Q}\hookrightarrow\mathbb C_p$ with $p\notin S_0$. An integer is supported on $S_0$ if it is positive and every prime dividing it belongs to $S_0$. A sesquilinear form and additive subgroup satisfy the integral quadratic condition at $d$ when the form is Hermitian, $\operatorname{Im}H(x,y)\in\mathbb Z$ for $x,y$ in the subgroup, and $\sqrt d\operatorname{Re}H(x,x)/2\in\mathbb Z$ there.
