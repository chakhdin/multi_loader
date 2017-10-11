LOAD DATA 
APPEND
   INTO TABLE TMP_BLOCK_TRANSACTIONS
   FIELDS TERMINATED BY ',' TRAILING NULLCOLS
   (
	BLOCK_HEADER_REF,
	BLOCK_TRANSACTION_REF,
	TX_HASH,
	TX_VERSION,
	TX_IN_COUNT,
	TX_OUT_COUNT,
	TX_LOCK_TIME,
	TX_COINBASE_FLAG
	)
--sqlldr.exe userid=btc_user/btc_user@fiatdev direct=true control=../tx.ctl log=../log/tx.log bad=tx.bad
