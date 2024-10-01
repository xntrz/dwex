# https://dwarfstd.org/doc/dwarf_1_1_0.pdf

#
#	Fund types
#
DW_FT_char 				= 0x0001
DW_FT_signed_char 		= 0x0002
DW_FT_unsigned_char		= 0x0003
DW_FT_short				= 0x0004
DW_FT_signed_short 		= 0x0005
DW_FT_unsigned_short 	= 0x0006
DW_FT_integer 			= 0x0007
DW_FT_signed_integer	= 0x0008
DW_FT_unsigned_integer 	= 0x0009
DW_FT_long 				= 0x000a
DW_FT_signed_long 		= 0x000b
DW_FT_unsigned_long		= 0x000c
DW_FT_pointer 			= 0x000d
DW_FT_float				= 0x000e
DW_FT_dbl_prec_float 	= 0x000f
DW_FT_ext_prec_float 	= 0x0010
DW_FT_complex 			= 0x0011
DW_FT_dbl_prec_complex 	= 0x0012
DW_FT_void 				= 0x0014
DW_FT_boolean 			= 0x0015
DW_FT_ext_prec_complex 	= 0x0016
DW_FT_label				= 0x0017

#
#	Fund types mod
#
DW_FT_MOD_pointer_to	= 0x01
DW_FT_MOD_reference_to	= 0x02
DW_FT_MOD_const			= 0x03
DW_FT_MOD_volatile		= 0x04


DW_FT = {
	DW_FT_char				: 'char',
	DW_FT_signed_char		: 'signed char',
	DW_FT_unsigned_char		: 'unsigned char',
	DW_FT_short				: 'short',
	DW_FT_signed_short		: 'signed short',
	DW_FT_unsigned_short	: 'unsigned short',
	DW_FT_integer			: 'integer',
	DW_FT_signed_integer	: 'signed integer',
	DW_FT_unsigned_integer	: 'unsigned integer',
	DW_FT_long				: 'long',
	DW_FT_signed_long		: 'signed long',
	DW_FT_unsigned_long		: 'unsigned long',
	DW_FT_pointer			: 'void*',
	DW_FT_float				: 'float',
	DW_FT_dbl_prec_float	: 'double',
	DW_FT_void				: 'void',
	DW_FT_boolean			: 'bool',
}

DW_FT_MOD = {
	DW_FT_MOD_pointer_to	: '*',
	DW_FT_MOD_reference_to	: '&',
	DW_FT_MOD_const			: 'const',
	DW_FT_MOD_volatile		: 'volatile',
}