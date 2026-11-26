---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/IsGrRefl.lean",
  "declarations": [
    "UpperTheory.Gal.Int.Geo.CongAt",
    "UpperTheory.Gal.Int.Geo.Cover",
    "UpperTheory.Gal.Int.Geo.GoodAt",
    "UpperTheory.Gal.Int.Geo.Nice"
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

## Schemes with correspondences and the Galois representations they carry

[Definition / hypothesis AGR.D080](https://andrewodesky.com/rh/lean/GlobalTheory.GalV.HTower/)

Throughout, $k$ is a field, $\ell$ a prime, $\bar k$ an algebraic closure of $k$, and $\overline{\mathbb Q}_\ell$ an algebraic closure of $\mathbb Q_\ell$.

**Scheme with correspondences.** A *scheme with correspondences* over $k$ is a tuple $H=(Z,\Gamma,(Y_g,s_g,t_g)_{g\in\Gamma})$ consisting of a scheme $Z$ with a morphism $q\colon Z\to\operatorname{Spec}k$, a set $\Gamma$, and for each $g\in\Gamma$ a scheme $Y_g$ with two morphisms $s_g,t_g\colon Y_g\to Z$ such that $q\,s_g=q\,t_g$. A morphism of schemes is *finite étale of degree $d$* if it is finite, étale, and every geometric point of the target has exactly $d$ preimages. We call $H$ *smooth projective* if $q$ is smooth, $Z$ admits a closed immersion over $k$ into some $\mathbb P^N_k$, and every $s_g$ is finite étale of some degree $d_g$. For a field $K$ and a ring homomorphism $\tau\colon k\to K$, the base change $H_\tau$ has $Z_\tau=Z\times_{k,\tau}K$, the same index set, and the base changes of the $Y_g$, $s_g$, $t_g$.

**Cohomology and the operators $T_g$.** Put $Z_{\bar k}=Z\times_k\bar k$ and $$W_\ell(H)=\bigoplus_{n\in\mathbb Z}H^n(Z_{\bar k},\mathbb Q_\ell),\qquad H^n(X,\mathbb Q_\ell)=\Big(\varprojlim_m H^n_{\text{ét}}(X,\mathbb Z/\ell^m)\Big)\otimes_{\mathbb Z_\ell}\mathbb Q_\ell .$$ The group $\operatorname{Aut}(\bar k/k)$ acts $\mathbb Q_\ell$-linearly on $W_\ell(H)$ by $\sigma\mapsto(\mathrm{id}_Z\times\operatorname{Spec}\sigma)^*$. For $g\in\Gamma$, a $\mathbb Q_\ell$-linear endomorphism $T$ of $W_\ell(H)$ *is induced by $g$* if there are a finite étale surjective morphism $c\colon X\to Z_{\bar k}$, Galois for a finite group acting on $X$, a finite set $J$ and morphisms $\sigma_j\colon X\to Y_{g,\bar k}$ ($j\in J$) with $s_g\sigma_j=c$ such that $\coprod_{j\in J}X\to Y_{g,\bar k}\times_{Z_{\bar k}}X$ is an isomorphism, and $$c^*(Tx)=\sum_{j\in J}(t_g\sigma_j)^*x\qquad\text{for all }x\in W_\ell(H).$$ This is the usual operator $s_{g*}t_g^*$ of the correspondence $(Y_g,s_g,t_g)$. We let $T_g$ be an endomorphism induced by $g$, chosen once.

**Eigenspace.** For a function $\theta\colon\Gamma\to\overline{\mathbb Q}_\ell$ put $$V_\theta=\{x\in\overline{\mathbb Q}_\ell\otimes_{\mathbb Q_\ell}W_\ell(H)\;:\;(1\otimes T_g)x=\theta(g)x\text{ for all }g\in\Gamma\}.$$

**Representation carried by $(H,\theta)$.** Let $d\ge 0$. A homomorphism $\rho\colon\operatorname{Aut}(\bar k/k)\to GL_d(\overline{\mathbb Q}_\ell)$ *is carried by $(H,\theta)$* if there are a basis $b_1,\dots,b_d$ of $V_\theta$ (so $\dim V_\theta=d$), a homomorphism $\rho_0\colon\operatorname{Aut}(\bar k/k)\to GL_d(\overline{\mathbb Q}_\ell)$ with $\sigma b_j=\sum_i\rho_0(\sigma)_{ij}b_i$ for all $\sigma$ and $j$, and a function $c\colon\{1,\dots,d\}\to\mathbb N$ such that for all $\sigma$: $\rho_0(\sigma)_{ij}=0$ whenever $c(j)<c(i)$, and $\rho(\sigma)_{ij}=\rho_0(\sigma)_{ij}$ if $c(i)=c(j)$, $\rho(\sigma)_{ij}=0$ otherwise. Thus $\rho$ is the direct sum of the graded pieces of a flag in $V_\theta$ stable under $\operatorname{Aut}(\bar k/k)$.

From here on $k=E$ is a number field, $w$ a finite place of $E$, and $O_{(w)}\subset E$ the valuation ring of $w$. The coefficient field $L$ of $\theta\colon\Gamma\to L$ may be any field.

**Model at $w$.** A *model of $(H,\theta)$ at $w$* consists of

- a scheme $\mathcal Y$ with a morphism $u\colon\mathcal Y\to\operatorname{Spec}O_{(w)}$ that is smooth of some constant relative dimension and factors through a closed immersion into some $\mathbb P^N_{O_{(w)}}$;
- a morphism $\pi\colon Z\to\mathcal Y$ lying over $\operatorname{Spec}E\to\operatorname{Spec}O_{(w)}$ such that the induced morphism $\pi_E\colon Z\to\mathcal Y\times_{O_{(w)}}E$ is finite étale;
- a finite group $\Delta$ and morphisms $a(\delta)\colon Z\to Z$ ($\delta\in\Delta$) with $a(1)=\mathrm{id}$, $a(\delta\delta')=a(\delta')\circ a(\delta)$, $\pi_E\circ a(\delta)=\pi_E$, such that $\coprod_{\delta\in\Delta}Z\to Z\times_{\mathcal Y_E}Z$, $z\mapsto(a(\delta)z,z)$ on the $\delta$-th copy, is an isomorphism;
- for every $\delta\in\Delta$ an index $g\in\Gamma$ such that $s_g$ is an isomorphism, $t_g=a(\delta)\circ s_g$ and $\theta(g)=1$.

The model is *surjective* if $\pi_E$ is surjective; then $\pi_E$ is a Galois covering with group $\Delta$.

**Correspondences over the model.** Let $(T,a,b)$ be a scheme $T$ with two morphisms $a,b\colon T\to\mathcal Y$, and let $m\ge 1$. We say that $g\in\Gamma$ *lies over $(T,a,b)$ with multiplicity $m$* if there is a morphism $\kappa\colon Y_g\to T$ with $a\kappa=\pi s_g$ and $b\kappa=\pi t_g$ such that $(s_g,\kappa)\colon Y_g\to Z\times_{\pi,\mathcal Y,a}T$ is finite étale of degree $m$. The correspondences of $H$ *descend to the model* if every $g\in\Gamma$ lies, with some multiplicity, over some $(T,a,b)$ with $ua=ub$ and $a$ finite étale of some degree.

**Good reduction at $w$.** $(H,\theta)$ has *good reduction at $w$* if it has a surjective model at $w$ to which the correspondences of $H$ descend. It has *weak good reduction at $w$* if it has a model at $w$, not necessarily surjective, to which they descend.

**Congruence relation.** Let $n\ge 0$ and $\vartheta=(\vartheta_0,\vartheta_1,\dots)$ a sequence in $L$. Let $p$ be the residue characteristic of $w$ and $q=N(w)=p^f$. A model of $(H,\theta)$ at $w$ *satisfies the congruence relation of degree $n$ with coefficients $\vartheta$* if there are an irreducible element $\varpi$ of $O_{(w)}$, and for $j=0,\dots,n$ a scheme $T_j$ with morphisms $a_j,b_j\colon T_j\to\mathcal Y$, an index $\gamma_j\in\Gamma$ and an integer $m_j\ge1$, such that:

1. $a_j$ is finite, étale over the open subscheme of $\mathcal Y$ where $p$ is invertible, and has a constant number of points in the fibre over every geometric point of $\mathcal Y$ of characteristic different from $p$; and $ua_j=ub_j$;
2. $\gamma_j$ lies over $(T_j,a_j,b_j)$ with multiplicity $m_j$, and $\theta(\gamma_j)=m_j\vartheta_j$;
3. (point identity) for every valuation ring $V$ with algebraically closed fraction field of characteristic different from $p$, with residue field $\kappa$, every $y\colon\operatorname{Spec}V\to\mathcal Y$ sending the closed point to a generic point of the closed subset $\{\varpi=0\}$ of $\mathcal Y$, and such that the set $I_j$ of morphisms $z\colon\operatorname{Spec}V\to T_j$ with $a_jz=y$ is finite for every $j$, the following two multisets of $\kappa$-valued points of $\mathcal Y$ are equal: $$\sum_{j\text{ even}}q^{\binom j2}\sum_{z\in I_j}\big[F^{\,n-j}(\overline{b_jz})\big]\;=\;\sum_{j\text{ odd}}q^{\binom j2}\sum_{z\in I_j}\big[F^{\,n-j}(\overline{b_jz})\big].$$ Here $\bar x$ is the restriction of a $V$-valued point $x$ to $\operatorname{Spec}\kappa$, and $F$ sends a $\kappa$-valued point $x$ to $x\circ\operatorname{Spec}(\varphi)$ with $\varphi(c)=c^q$ on $\kappa$ (the identity is required only when $c\mapsto c^q$ is a ring endomorphism of $\kappa$).

$(H,\theta)$ *satisfies the congruence relation of degree $n$ with coefficients $\vartheta$ at $w$* if some surjective model at $w$ does; it satisfies it *weakly* if some model at $w$ does.

**Hecke polynomial and its roots.** For $\vartheta$ with values in $\overline{\mathbb Q}_\ell$ put $P_{w,n,\vartheta}(X)=\sum_{j=0}^n(-1)^jq^{\binom j2}\vartheta_jX^{n-j}$. Given a ring isomorphism $\iota\colon\overline{\mathbb Q}_\ell\to\mathbb C$, a finite multiset $R$ of complex numbers is *the multiset of roots of $P_{w,n,\vartheta}$* if $\vartheta_0\neq0$ and $\iota(P_{w,n,\vartheta})=\iota(\vartheta_0)\prod_{r\in R}(X-r)$.

**Occurrence in Hodge degree $j$.** Let $\tau\colon E\to\mathbb C$ be an embedding, $\iota\colon\overline{\mathbb Q}_\ell\to\mathbb C$ a ring isomorphism, $\theta\colon\Gamma\to\overline{\mathbb Q}_\ell$ and $j\in\mathbb Z$. We say *$\theta$ occurs in Hodge degree $j$ at $\tau$* if $j\ge0$, every $s_g$ (after base change along $\tau$) is finite étale, and for some $i\ge0$ there is a nonzero $x\in H^i(Z_\tau,\Omega^j_{Z_\tau/\mathbb C})$ with $\operatorname{tr}_{s_g}(t_g^*x)=\iota(\theta(g))\,x$ for all $g\in\Gamma$.
