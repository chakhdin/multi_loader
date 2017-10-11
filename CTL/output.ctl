LOAD DATA 
APPEND
   INTO TABLE TMP_TRANSACTION_OUTPUTS
   FIELDS TERMINATED BY ',' TRAILING NULLCOLS
   (
	BLOCK_HEADER_REF filler,
	BLOCK_TRANSACTION_REF,
	TRANSACTION_OUTPUT_REF,
	TX_HASH,
	OUTPUT_INDEX,
	AMOUNT,
	PK_SCRIPT_SIZE,
	PK_SCRIPT_TYPE,
	BPK_SCRIPT CHAR(4000)
	)
--sqlldr.exe userid=btc_user/btc_user@fiatdev direct=true control=../output.ctl log=../log/output.log bad=output.bad
