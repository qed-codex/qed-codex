---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/AdelCOfInnerProductFormula.lean",
  "declarations": [
    "GlobalTheory.LowRow.scalar_of_form_key_lowC"
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

## Lower bound for the theta scalar

[Theorem THETA.1122](https://andrewodesky.com/rh/lean/GlobalTheory.LowRow.scalar_of_form_key_lowC/)

Fix a CM field $E$, $f=[E:\mathbb Q]/2$, an initial rank $k$, a lift index $i$, definite and indefinite Hermitian spaces $V,W$, and the matched theta data specified in the conventions below. Write $n_V=\dim_E V$, $r=\dim_E W$, $g_0,g_1$ for the two level primes and $\mathrm{rd}_E$ for the root discriminant. Let $\mathscr H$ be the Hilbert space realizing the selected automorphic forms on $U(W)$, let $C$ be the finite-dimensional coefficient representation for $U(V)$, and let $X$ be any finite-dimensional complex inner-product space. Fix a linear map $\Theta:X\to\mathscr H$.

At each embedding $\tau$ in the CM type, let $V_\tau^{\mathrm{low}}$ be the lowest compact type of the discrete-series model of $U(W)_\tau$, and let $d_\tau=\dim V_\tau^{\mathrm{low}}$. Let $\delta$ be the specified product of minors in the oscillator polynomial space. For a tensor of lowest-type vectors $v$ and a coefficient vector $z\in C$, write $\Phi_{v,z}$ for the Schwartz function obtained from the coefficient map and the fixed finite Schwartz vector $\varphi$. For $U\in\mathscr H$, write $U(v)$ for its associated scalar automorphic form and $$T_{v,z}U(h)=\int_{[U(W)]}\theta(h,g;\Phi_{v,z})\,\overline{U(v)(g)}\,dg$$ for the scalar theta integral with the fixed measures. Assume all the following packages of identities, for every matched datum and every compatible choice of frames, covolume-one oscillator measure, real Haar measures and unit lowest-type vectors:

1. The theta inner-product identity: its defining integrals are integrable, the unfolded sum is absolutely integrable, and the $L^2$ pairing of two theta integrals equals the volume of the $U(V)$ quotient times the integral over the real $U(W)$ factors of the sum over finite $U(W)$ classes of the oscillator pairing times the conjugate Petersson pairing of the translated forms.
2. The Fock coefficient identity: the oscillator pairing of the functions associated with $(v,z)$ and $(v',z')$, after finite translation $y$ and real translation $g=(g_\tau)$, is $$\|\delta\|_F^2\prod_\tau\langle v'_\tau,\pi_\tau(g_\tau)v_\tau\rangle\,\langle z',z\rangle\,\langle\omega(1,y)\varphi,\varphi\rangle.$$ Here $\omega$ is the Weil representation and $\|\cdot\|_F$ is the Fischer norm.
3. The minor norm identity is $\|\delta\|_F^2=\prod_\tau\mathcal H(\lambda^+_\tau)\mathcal H(\lambda^-_\tau)$, where $\lambda^\pm_\tau$ are the two partitions specifying the minors in $\delta$ and $\mathcal H$ is the product of their hook lengths.
4. For every nonzero selected Hecke subspace, the finite translated sum in condition 1 converges to $$|P|\,\|\varphi\|^2\,\frac{Z^S}{d^S}\,\overline{\langle U_1(v_1),U_2(v_2)\rangle_{\mathrm{Pet}}}.$$ Here $P$ is the finite level subgroup, $S$ is the finite set of bad places, $d^S=\prod_{v\notin S}d_v$, where $d_v=\prod_{t<h\le n_V}(1-\chi_v^h(\operatorname{Norm}v)^{-h})^{-1}$ and $\chi_v=1$ if $v$ splits in $E$, $-1$ otherwise; and $Z^S=\prod_{w\nmid S}\prod_{a=1}^r(1-x_{w,a})^{-1}$ with parameters satisfying $|x_{w,a}|\le(\operatorname{Norm}w)^{(r-1)/2-(1+t)/2}$; $t$ is the auxiliary rank parameter of the matched datum.
5. The level $K_V$ on $U(V)$ is contained in the stabilizer $K_V^0$ of the definite lattice, and $$[K_V^0:K_V]\,\|\varphi\|^2=\prod_{w\in S}d_w^{-1}.$$ The factors $d_w$ are the local denominator factors of the same normalization.
6. The definite mass satisfies $\operatorname{mass}(V,K_V^0)\ge1/(w_E^{n_V}n_V!)$, where $w_E$ is the number of roots of unity in $E$.
7. For each real factor and unit lowest-type vector, the squared matrix coefficient is integrable, its integral $I_\tau$ is positive, and $$\log I_\tau^{-1}\le2+r^2\log\bigl(2\sqrt2\,r^2n_V(\deg_\tau+2)\bigr).$$ Here $\deg_\tau$ is the total degree of the oscillator minor polynomial at that embedding.

Let $b\in\mathbb R$ and assume, for every $\tau$, that the lift weight $e_{i,\tau}$ lies in $(0,2b]$, every source weight parameter $v_{\tau,j}$ lies in $[0,b]$, and every target parameter $b_{\tau,j}$ satisfies $|b_{\tau,j}-e_{i,\tau}|\le b$. Require $(kb)^8\le g_0,g_1$.

In addition, for every orthonormal basis $(z_j)$ of $C$, every tensor $v$ of unit lowest-type vectors, and all $U_1,U_2\in\mathscr H$, assume the identity tying the given map to these theta integrals: $$\langle\Theta^*U_1,\Theta^*U_2\rangle=\left(\prod_\tau d_\tau\right)^2\sum_j\langle T_{v,z_j}U_1,T_{v,z_j}U_2\rangle_{L^2([U(V)])}.$$ Let $H_0$ be the subspace with the chosen level character and Hecke eigenvalues, and assume $H_0\ne0$. Let $\Theta^*_{\mathrm{lev}}=|P|^{-1}\Theta^*$ be the adjoint divided by the cardinality of the finite level subgroup, with inverse zero if that cardinality is zero. Then there exists $\kappa_\Theta>0$ such that $$\Theta\Theta^*_{\mathrm{lev}}z=\kappa_\Theta z\quad(z\in H_0),$$ $$\log\kappa_\Theta\ge\sum_\tau\log\bigl(\mathcal H(\lambda^+_\tau)\mathcal H(\lambda^-_\tau)\bigr)-8fn_V^2\log(b\,\mathrm{rd}_Eg_0g_1n_V).$$
