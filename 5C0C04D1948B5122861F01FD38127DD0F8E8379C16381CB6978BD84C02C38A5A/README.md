## Initial Analysis
When I opened the file in DIE (detect it easy) it said that the file was .NET, so I opened it in DnSpy(ex), but nothing interesting was found:
```C#
using System;
using System.CodeDom.Compiler;
using System.ComponentModel;
using System.Configuration;
using System.Diagnostics;
using System.Runtime.CompilerServices;

namespace SpoofMe.My
{
	// Token: 0x02000006 RID: 6
	[CompilerGenerated]
	[GeneratedCode("Microsoft.VisualStudio.Editors.SettingsDesigner.SettingsSingleFileGenerator", "11.0.0.0")]
	[EditorBrowsable(EditorBrowsableState.Advanced)]
	internal sealed class MySettings : ApplicationSettingsBase
	{
		// Token: 0x06000011 RID: 17 RVA: 0x0001F1BC File Offset: 0x00000000
		[DebuggerNonUserCode]
		[EditorBrowsable(EditorBrowsableState.Advanced)]
		private static void C185B8A1(object 90ADE639, EventArgs E99BA3B0)
		{
		}

		// Token: 0x17000008 RID: 8
		// (get) Token: 0x06000012 RID: 18 RVA: 0x0001F1F8 File Offset: 0x00000000
		public static MySettings Default
		{
			get
			{
			}
		}

		// Token: 0x04000008 RID: 8
		private static MySettings C133190A;

		// Token: 0x04000009 RID: 9
		private static bool BC9245A8;

		// Token: 0x0400000A RID: 10
		private static object 1034E0BE;
	}
}
```
Also, I don't know C# lol. Anyways, the crackme description, "Fool the system with a request substitution!" was kinda a big hint, so here's what I did (includes the solution):


https://github.com/Boberttt/notes/assets/104478197/d34cb401-9f28-4ab9-a9a9-a3135d418d0c

