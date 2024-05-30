# Simple-DES
Implementing DES algorithm encryption

## Implementing The Key Schedule module
<div align="justify">
The bellow algorithm specifies how to compute the DES round keys K<sub>i</sub>, each of which contains 48 bits of K. These operations make use of tables PC1 AND PC2, which are called permuted choice 1 and permuted choice 2. To begin, 8 bits of K are discarded (by PC1). the remaining 56 bits are permuted and assigned to two 28-bit variables C and D; and then for 16 iterations, both C and D are rotated either 1 or 2 bits, and 48 bits (K<sub>i</sub>) are selected from the concatenated result.
</div>

<div>
  

### PC1
|    |    |    |    |    |    |    |
|----|----|----|----|----|----|----|
| 57 | 49 | 41 | 33 | 25 | 17 |  9 |
|  1 | 58 | 50 | 42 | 34 | 26 | 18 |
| 10 |  2 | 59 | 51 | 43 | 35 | 27 |
| 19 | 11 |  3 | 60 | 52 | 44 | 36 |
| 63 | 55 | 47 | 39 | 31 | 23 | 15 |
|  7 | 62 | 54 | 46 | 38 | 30 | 22 |
| 14 |  6 | 61 | 53 | 45 | 37 | 29 |
| 21 | 13 |  5 | 28 | 20 | 12 |  4 |

### PC2
|    |    |    |    |    |    |
|----|----|----|----|----|----|
| 14 | 17 | 11 | 24 |  1 |  5 |
|  3 | 28 | 15 |  6 | 21 | 10 |
| 23 | 19 | 12 |  4 | 26 |  8 |
| 16 |  7 | 27 | 20 | 13 |  2 |
| 41 | 52 | 31 | 37 | 47 | 55 |
| 30 | 40 | 51 | 45 | 33 | 48 |
| 44 | 49 | 39 | 56 | 34 | 53 |
| 46 | 42 | 50 | 36 | 29 | 32 |

</div>
<div align="justify">

#### Algorithm DES key schedule

**INPUT**: 64-bit key K = k<sub>1</sub>...k<sub>64</sub> (including 8 odd-parity bits).  
**OUTPUT**: sixteen 48-bit keys K<sub>i</sub>, 1 ≤ i ≤ 16.

1. Define v<sub>i</sub>, 1 ≤ i ≤ 16 as follows: v<sub>i</sub> = 1 for i ∈ {1, 2, 9, 16}; v<sub>i</sub> = 2 otherwise.  
   (These are left-shift values for 28-bit circular rotations below.)
2. T ← PC1(K); represent T as 28-bit halves (C<sub>0</sub>, D<sub>0</sub>).  
   (Use PC1 to select bits from K: C<sub>0</sub> = k<sub>57</sub>k<sub>49</sub> ... k<sub>36</sub>, D<sub>0</sub> = k<sub>63</sub>k<sub>55</sub> ... k<sub>4</sub>.)
3. For i from 1 to 16, compute K<sub>i</sub> as follows:  
   C<sub>i</sub> ← (C<sub>i−1</sub> ←. v<sub>i</sub>), \( D<sub>i</sub> ← (D<sub>i−1</sub> ←. v<sub>i</sub>),  K<sub>i</sub> ← PC2(C<sub>i</sub>, D<sub>i</sub>).  
   (Use PC2 select 48 bits from the concatenation b<sub>1</sub>b<sub>2</sub> ... b<sub>56</sub>} of C<sub>i</sub> and D<sun>i</sub>; K<sub>i</sub> = b<sub>14</sub>b<sub>17</sub> ... b<sub>32</sub>. '←.' denotes left circular shift.)
  
</div>

## Implementing The DES Encryption

<div align="justify">
  DES is a Feistel cipher which processes plaintext blocks of n = 64 bits, producing 
  64-bit ciphertext bolcks. The effective size of the secret key is k = 56 bits; more   precisely, the input key K is specified as a 64-bit key, 8 bits of which (bits 8,     16, ..., 64) may be used as parity bits. The 2<sup>56</sup> keys implement (at        most) 2<sup>56</sup> of the 2<sup>64</sup>! possible bijectin on 64-bit blocks.       widely held belief is that the parity bits were introduced to reduce the effective    key size from 64 to 56 bits, to intentionally reduce the cost of exhaustive key   
  search by a factor of 256.
</div>

