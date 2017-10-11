LOAD DATA 
APPEND
   INTO TABLE TMP_OUTPUT_ADDRESSES
   FIELDS TERMINATED BY ',' TRAILING NULLCOLS
   (
	BLOCK_HEADER_REF filler,
	BLOCK_TRANSACTION_REF filler,
    TRANSACTION_OUTPUT_REF,
	OUTPUT_ADDRESS_REF,
	TX_HASH filler,
	OUTPUT_INDEX FILLER,
	ADDRESS_INDEX,
	PUBLIC_KEY,
	ADDRESS,
	ADDRESS_TYPE
	)
--sqlldr.exe userid=btc_user/btc_user@fiatdev direct=true control=../addr.ctl log=../log/addr.log bad=addr.bad

