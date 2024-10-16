using System;
using Sandbox.ModAPI;

namespace ModTemplate
{
    public class Constants
    {
        public static Guid ModGuid = new Guid("F7EA06E6-FC5B-4777-AF67-D3E8BB9D24D2");
        public static bool IsClient => !MyAPIGateway.Session.IsServer;
        public static bool IsServer => MyAPIGateway.Session.IsServer;
        public static bool IsDedicated => MyAPIGateway.Session.IsServer && MyAPIGateway.Utilities.IsDedicated;
        public static bool HasCreativeRights => MyAPIGateway.Session.CreativeMode || MyAPIGateway.Session.HasCreativeRights;
        public static long PlayerIdentityId => MyAPIGateway.Session.Player.IdentityId;
    }
}