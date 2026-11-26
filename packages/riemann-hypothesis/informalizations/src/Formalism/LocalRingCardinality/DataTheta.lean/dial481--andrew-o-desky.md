---
{
  "module": "src/Formalism/LocalRingCardinality/DataTheta.lean",
  "declarations": [
    "Formalism.BasicNotions.TH.DSRep",
    "Formalism.BasicNotions.TH.FockData",
    "Formalism.BasicNotions.TH.GKMod",
    "Formalism.BasicNotions.TH.GrpData",
    "Formalism.BasicNotions.TH.ProvA",
    "Formalism.BasicNotions.TH.URep",
    "Formalism.BasicNotions.ThetaX"
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

## Hermitian theta spaces and pairings

[Definition / hypothesis ARAK.D123](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.ThetaX/)

Hypothesis (theta spaces). Use ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)), ([Hermitian spaces in the theta constructions](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.CMData/)), ([Column chains and period pairings](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Member/)), and ([Complex vector spaces and integral spans](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Rows.Data/)). Write $E/F$ for the CM extension, $\Sigma$ for its selected CM type, $z$ for a source index and $\mu$ for a twist index, with distinguished index $\mu_0$. A Hermitian space below includes its specified basis, signature function and unimodular integral lattice as in ([Hermitian spaces in the theta constructions](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.CMData/)).

For every Hermitian $E$-space $V$, choose a complex vector space $\mathcal A(V)$, a subspace $\mathcal C(V)$, and a pairing $$P_V:\mathcal A(V)\times\mathcal C(V)\longrightarrow\mathbb C.$$ The pairing is conjugate linear in its first variable and linear in its second. Its restriction to $\mathcal C(V)$ is Hermitian, and $\Re P_V(F,F)>0$ for nonzero $F\in\mathcal C(V)$.

For each $\tau\in\Sigma$ and every complex square matrix $g$ of size $\dim_E V$, there is an endomorphism $R_{V,\tau}(g)$ of $\mathcal A(V)$. Require $R_{V,\tau}(1)=1$. When $g,h$ preserve the embedded Gram form, require $R_{V,\tau}(gh)=R_{V,\tau}(g)R_{V,\tau}(h)$ and preservation of $\mathcal C(V)$. There is a group $G_f(V)$ with a representation $R_f$ on $\mathcal A(V)$ preserving $\mathcal C(V)$ and commuting with every $R_{V,\tau}(g)$. For each finite set $S$ of places of $F$, choose a subgroup $K^S(V)\subseteq G_f(V)$, with $K^{S'}(V)\subseteq K^S(V)$ whenever $S\subseteq S'$. For every array $\Pi=(\Pi_\tau)_{\tau\in\Sigma}$ of finite subsets of $\mathbb Q\times\{0,1\}$, choose a subspace $\mathcal A(V)[\Pi]$.

There is an abelian group $\mathcal X$, with additive rational infinity weights $\nu_\tau:\mathcal X\to\mathbb Q$. For every $\mu$ and nonnegative $j$, choose $\chi_{\mu,j}\in\mathcal X$, with $$\nu_\tau(\chi_{\mu,j+1})=-e_{\tau,j}\qquad(0\le j<m).$$ Choose $\eta\in\mathcal X$ with $\nu_\tau(\eta)\in\{1/2,-1/2\}$ and, separately, $\nu_\tau(\eta)=1/2$ for every $\tau$. The integers $e_{\tau,j}$ are the Hermitian weights in ([Column chains and period pairings](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Member/)).

For every pair $V,W$, there is a complex vector space $\mathcal S(V,W)$ with a designated subset $\mathcal F(V,W)$ and a designated subspace $\mathcal S_{\rm fin}(V,W)$. For $\chi,\chi'\in\mathcal X$, there is a bilinear map $$\Theta_{V,W}^{\chi,\chi'}:\mathcal S(V,W)\times\mathcal C(V)\longrightarrow\mathcal A(W).$$ For all nonnegative integers $t',j$, choose Hermitian spaces $X_{t',j},Y_{t',j}$ and $E$-linear maps $i_{t',j}:X_{t',j}\to Y_{t',j}$. For $j\le m$, $$\dim_E X_{t',j}=k+j(t'+1),\qquad \dim_EY_{t',j}=r+jt'.$$ For $j\le m$, at every embedding the specified signature of each space is the signature of its embedded Gram matrix; $X_{t',j}$ is definite, with either signature $(\dim X_{t',j},0)$ or $(0,\dim X_{t',j})$. The maps $i_{t',j}$ are isometric for $j<m$. There is an isometric map $Y_{t',m}\to X_{t',m}$ for every $t'$. There are further Hermitian spaces $Y^-_{t',j,h}$ for all nonnegative $t',j,h$, with $Y^-_{t',j,0}=Y_{t',j}$. For the selected integer $t$ and $j\le m$, require $X_{t,j}=X_j$ and $Y_{t,j}=Y_j$, using the spaces of ([Hermitian spaces in the theta constructions](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.CMData/)).

Each $\mathcal A(V)$ has an additive conjugate-linear involution preserving $\mathcal C(V)$. For every $E$-linear map $i:A\to B$, choose a set $\mathcal P(i)$ and a complex vector space $\mathcal J(i)$. For $p\in\mathcal P(i)$ and $s\in\mathcal J(i)$, choose a pairing $$B_{i,p,s}:\mathcal A(A)\times\mathcal C(B)\longrightarrow\mathbb C$$ conjugate linear in the first argument and linear in the second. If the nonnegative integer difference $\max(0,\dim B-\dim A)$ is odd, this pairing is independent of $s$. For every $E$-linear $i:B\to A$, choose another pairing $B_i^{\rm top}$ on the same two spaces, with the same sesquilinearity. For every $z$, choose two elements $p_z,p'_z\in\mathcal P(X_0\to Y_0)$.

For every $z,\mu,j$, there is a linear map $c_{z,\mu,j}:H_z\to\mathcal C(X_j)$ from the initial source Hermitian space. For every $\mu,j$, there is a linear map $r_{\mu,j}:B_{\mu,j}\to\mathcal C(Y_j)$ from the row multiplicity space. Choose $$\Phi_{\mu,j}\in\mathcal S(Y_{j+1},Y_j),\qquad \Phi^+_{\mu,j}\in\mathcal S(Y_j,Y_{j+1}),\qquad m_{\mu,j}>0,$$ with $m_{\mu_0,j}=1$ and $m_{\mu,0}=1$ for all indices.

## Abstract oscillator representations and theta maps

[Definition / hypothesis ARAK.D152](https://andrewodesky.com/rh/lean/Formalism.L2.Theta.AllTied/)

Hypothesis (abstract oscillator and theta comparison). Impose ([Hermitian theta spaces and pairings](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.ThetaX/)) and all the representation choices, Haar and parameter comparisons of ([Archimedean double covers and oscillator representations](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.TH.GrpData/)). On these same spaces, characters, test vectors, groups and measures impose ([Automorphic theta functions and their measures](https://andrewodesky.com/rh/lean/Formalism.L2.Theta.ThetaTied/)), the smooth-realization and type comparisons of ([Smooth automorphic functions and discrete-series types](https://andrewodesky.com/rh/lean/Formalism.L2.Theta.ThetaSmoothnessCondition/)), the unequal-rank oscillator laws, unramified-vector laws and prescribed-vector transpose identity of ([Adelic oscillator actions and theta integrals](https://andrewodesky.com/rh/lean/Formalism.L2.Theta.WeilTied/)), ([Polynomial Fock vectors and compact frames](https://andrewodesky.com/rh/lean/Formalism.L2.Theta.KfinTied/)), and ([Bessel flags and their period integrals](https://andrewodesky.com/rh/lean/Formalism.L2.Theta.BesDat/)). All choices referred to in these hypotheses are common choices throughout.

Hypothesis (equal-rank theta comparison), when separately imposed, adds the equal-rank oscillator laws of ([Adelic oscillator actions and theta integrals](https://andrewodesky.com/rh/lean/Formalism.L2.Theta.WeilTied/)) for these same choices.

## Archimedean double covers and oscillator representations

[Definition / hypothesis ARAK.D157](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.TH.GrpData/)

Write $I_{p,q}=\{0,\ldots,p-1\}\sqcup\{0,\ldots,q-1\}$, with its two signed blocks, $J=\operatorname{diag}(1_p,-1_q)$ and $\mathfrak u(p,q)=\{X:X^*J+JX=0\}$. Compact matrices are block diagonal. A positive compact matrix unit $E_{ab}$ has $a<b$ in the same block.

**Double-cover group data.** For fixed $p,q\ge0$, a double-cover group datum consists of a topological group $\widetilde U(p,q)$ with its Borel measurable structure and a Haar measure $\widetilde\mu_{p,q}$. Choose homomorphisms $c:\widetilde U(p,q)\to\operatorname{GL}_{p+q}(\mathbb C)$ and $s:\widetilde U(p,q)\to\mathbb C^\times$ with $c(g)^*Jc(g)=J$ and $s(g)^2=\det c(g)$. For every $u\in U(p,q)$ and square root $z$ of $\det u$ there is exactly one $g$ with $(c(g),s(g))=(u,z)$. The map $(c,s)$ is a topological embedding. Choose a map $\mathcal E$ on all complex matrices, continuous on $\mathfrak u(p,q)$, such that $$c(\mathcal E(X))=e^X\ (X\in\mathfrak u(p,q)),\qquad\mathcal E(0)=1,\qquad\mathcal E((a+b)X)=\mathcal E(aX)\mathcal E(bX)\quad(X\in\mathfrak u(p,q),\ a,b\in\mathbb R).$$ **Unitary representations.** A unitary representation datum over a double-cover group datum consists of a complex Hilbert space $H$ and a strongly continuous norm-preserving representation $\pi$ of that group by bounded complex-linear operators.

**Lie module data.** A Lie module datum consists of a complex vector space $M$ and a complex-linear action $A:\mathfrak{gl}_{p+q}(\mathbb C)\to\operatorname{End}_{\mathbb C}(M)$ preserving brackets. Every vector of $M$ belongs to a finite-dimensional subspace stable under all block-diagonal matrices, and the rational weight spaces for the diagonal $E_{aa}$ span $M$.

**Square-integrable data.** Over a fixed double-cover group datum, square-integrable data consist of a unitary representation datum $(H,\pi)$ with $H\ne0$ whose only closed invariant complex subspaces are zero and the whole space, a positive real number $d$, a Lie module datum $(M,A)$ and an injective complex-linear map $i:M\to H$. For every $x,y\in H$, the squared matrix coefficient is integrable and $$\int|\langle y,\pi(g)x\rangle|^2d\widetilde\mu_{p,q}(g)=\frac{\|x\|^2\|y\|^2}{d}.$$ The image of $i$ consists exactly of vectors whose orbit under $c^{-1}(U(p)\times U(q))$ spans a finite-dimensional space. For $X\in\mathfrak u(p,q)$ and $v\in M$ require $$\left.\frac d{dt}\pi(\mathcal E(tX))i(v)\right|_{0}=i(A(X)v).$$

**Parameters.** A parameter is an injective rational array $\lambda:I_{p,q}\to\mathbb Q$, strictly decreasing within each signed block, with $2\lambda_a\in\mathbb Z$ and $\lambda_a-\lambda_b\in\mathbb Z$ for every $a,b$.

Hypothesis (archimedean representation choices). For every $p,q\ge0$, choose a double-cover group datum. For every rational array $\lambda:I_{p,q}\to\mathbb Q$, choose square-integrable data over this group, with notation $(H_\lambda,\pi_\lambda,d_\lambda,M_\lambda,A_\lambda,i_\lambda)$.

For every $p,q,r,s$, choose a complex Hilbert space $\mathcal H$ with a strongly continuous unitary representation $\Omega$ of $\widetilde U(pr+qs,ps+qr)$, and an injective linear map $i$ with dense image from the polynomial ring in variables $x_{ab}$ indexed by $I_{p,q}\times I_{r,s}$. Its monomial inner products are $$\langle i(x^\alpha),i(x^\beta)\rangle=\mathbf1_{\alpha=\beta}\prod_l\alpha_l!.$$ For a same-sign pair $l=(a,b)$ put $L_l=\partial_l$, $R_l=x_l$; for an opposite-sign pair put $L_l=x_l$, $R_l=-\partial_l$. Define $$\omega(Z)=\sum_{l,l'}Z_{ll'}\left(R_lL_{l'}+\tfrac12\mathbf1_{l=l'}\right).$$ Order same-sign pairs first, with the positive-positive pairs followed by negative-negative pairs; order opposite-sign pairs as positive-negative followed by negative-positive, using row-major order within each pair of blocks. In these coordinates require $$\left.\frac d{dt}\Omega(\mathcal E(tZ))i(P)\right|_0=i(\omega(Z)P)$$ for every real unitary Lie algebra element $Z$. Choose a homomorphism $j:\widetilde U(p,q)\times\widetilde U(r,s)\to\widetilde U(pr+qs,ps+qr)$ whose cover is the Kronecker product $c(g)\otimes c(h)$ in this ordering, and with $$s(j(g,h))=s(g)^{r+s}s(h)^{p+q}.$$ The two polynomial Lie actions obtained from this construction are $X\mapsto\omega(X\otimes1)$ and $Y\mapsto\omega(1\otimes Y)$.

Hypothesis (Haar and parameter compatibility). The image of $\widetilde\mu_{p,q}$ under $c$, viewed as a map to $U(p,q)$, is the specified measure $\mu^{\rm cd}_{p,q}$ of ([Formal degree with compact-dual normalization](https://andrewodesky.com/rh/lean/PositivityTheory.RgFd.B.formalDegreeCompactDual/)). Suppose $\lambda$ is a parameter. If $$|\lambda_a-\lambda_b|\ge120(p+q)\min(p,q)^{3/2}$$ for opposite-sign $a,b$, the chosen module contains a nonzero highest vector of weight $\Lambda=\lambda+\rho_{\rm nc}$, and $\Lambda$ minimizes $\sum_a(\mu_a+\rho_a)^2$ among all rational highest-vector weights $\mu$ in that module. Here $$\rho_a=\#\{b>a:b\text{ in the same block}\}-\#\{b<a:b\text{ in the same block}\},$$ $$2\rho_{{\rm nc},a}=\#\{b:\lambda_b<\lambda_a,\ b\text{ in the other block}\}-\#\{b:\lambda_a<\lambda_b,\ b\text{ in the other block}\}$$ $$\hspace{12mm}-\#\{b:\lambda_b<\lambda_a,\ b\text{ in the same block}\}+\#\{b:\lambda_a<\lambda_b,\ b\text{ in the same block}\}.$$ A highest vector of weight $\mu$ is a nonzero vector killed by each positive compact $A(E_{ab})$ and satisfying $A(E_{aa})v=\mu_av$.
