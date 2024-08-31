import discord
from discord.ext import commands
from discord import app_commands
from operation import MathService
from fromStr import large_num
from datetime import datetime

intent = discord.Intents.all()
intent.message_content = True
NumberFormat = commands.Bot(command_prefix="/", intents=intent)

@NumberFormat.event
async def on_ready():
    print(f"Logged in as {NumberFormat.user.name}")
    try:
        sync = await NumberFormat.tree.sync()
        print(f"Synced command(s): {len(sync)}")
    except Exception as e:
        print(f"Error syncing commands: {e}")

@NumberFormat.event
async def on_member_join(member):
    channel = NumberFormat.get_channel(1277823062825242647)

    if channel is not None:
        welcome_message = f"Welcome to the server, {member.mention}! Feel free to ask questions or make the server a better place with help requests."
        await channel.send(welcome_message)

    try:
        if member.dm_channel is None:
            await member.create_dm()
            invite_method = "https://discord.com/channels/1277823062825242644/1279100199171653702"
        dm_message = (
            f"Hello {member.display_name}, welcome to our server! 🎉\n"
            f"We're excited to have you here. If you have any questions, feel free to ask in the appropriate channels.\n "
            f"Here's a quick link to our server rules and guidelines: [Server Rules Link](<{invite_method}>). Enjoy your stay!"
        )
        await member.dm_channel.send(dm_message)

    except discord.Forbidden:
        print(f"Could not send DM to {member.display_name}. They might have DMs disabled.")

@NumberFormat.event
async def on_message(message):
    if message.author.bot:
        return
    
    if message.content == 'Create Rules!!!':
        if message.author.id in [1060813508608016436, 1278597357159710730]:
            embed = discord.Embed(
                title="Server Rules",
                description="Please follow these rules so u dont get warned",
                color = discord.Color.gold()
            )
            embed.add_field(name="1. Be Respectful", value="Treat everyone with respect.", inline=False)
            embed.add_field(name="2. No Spamming", value="Avoid spamming or flooding the chat.", inline=False)
            embed.add_field(name="3. No Harassment", value="Harassment of any kind will not be tolerated.", inline=False)
            embed.add_field(name="4. No False accusation", value="Will be setting up a scam-investigator soon?", inline=False)
            embed.set_footer(text="Thank you for being a part of our community!")
            channel = NumberFormat.get_channel(1279100199171653702)
            if channel:
                await channel.send(embed=embed)
            
                await message.delete()
                await message.channel.send("Rules embed created!", delete_after=5)
            else:
                await message.channel.send("You dont have permission todo this")
        else:
            try:
                await message.author.send("You dont have permission to use this command only Higher-Ups can use this")
            except discord.Forbidden:
                pass

@NumberFormat.event
async def on_member_remove(member):
    channel = NumberFormat.get_channel(1279095371062313082)
    if channel is not None:
        leaving = f"Hope to see u soon {member.display_name}"
        await channel.send(leaving)


@NumberFormat.tree.command(name="add", description="Add 2 values")
@app_commands.describe(value1="Number", value2="Number")
async def add(interaction: discord.Interaction, value1: str, value2: str):
    try:
        num1 = MathService.to_float(value1)
        num2 = MathService.to_float(value2)
    except ValueError:
        await interaction.response.send_message("Invalid input. Please provide valid numbers.")
        return

    from_larg = large_num()
    result = MathService.add(num1, num2)
    toStr = from_larg.toStr(result)
    
    new_title = "Result from adding value1 + value2"
    embed = discord.Embed(
        title=new_title,
        description=f"{value1} + {value2} = {result}",
        color=discord.Color.red()
    )
    embed.add_field(name="Result", value=result, inline=False)
    embed.add_field(name="To Short", value=toStr, inline=False)
    
    await interaction.response.send_message(embed=embed)

@NumberFormat.tree.command(name="sub", description="Sub 2 values")
@app_commands.describe(value1="Number", value2="Number")
async def sub(interaction: discord.Interaction, value1: str, value2: str):
    try:
        num1 = MathService.to_float(value1)
        num2 = MathService.to_float(value2)
    except ValueError:
        await interaction.response.send_message("Invalid input. Please provide valid numbers.")
        return

    from_larg = large_num()
    result = MathService.sub(num1, num2)
    toStr = from_larg.toStr(result)
    
    new_title = "Result from sub value1 - value2"
    embed = discord.Embed(
        title=new_title,
        description=f"{value1} - {value2} = {result}",
        color=discord.Color.red()
    )
    embed.add_field(name="Result", value=result, inline=False)
    embed.add_field(name="To Short", value=toStr, inline=False)
    
    await interaction.response.send_message(embed=embed)

@NumberFormat.tree.command(name="div", description="Add 2 values")
@app_commands.describe(value1="Number", value2="Number")
async def div(interaction: discord.Interaction, value1: str, value2: str):
    try:
        num1 = MathService.to_float(value1)
        num2 = MathService.to_float(value2)
    except ValueError:
        await interaction.response.send_message("Invalid input. Please provide valid numbers.")
        return

    from_larg = large_num()
    result = MathService.div(num1, num2)
    toStr = from_larg.toStr(result)
    
    new_title = "Result from dividing value1 / value2"
    embed = discord.Embed(
        title=new_title,
        description=f"{value1} / {value2} = {result}",
        color=discord.Color.red()
    )
    embed.add_field(name="Result", value=result, inline=False)
    embed.add_field(name="To Short", value=toStr, inline=False)
    
    await interaction.response.send_message(embed=embed)

@NumberFormat.tree.command(name="mul", description="mul 2 values")
@app_commands.describe(value1="Number", value2="Number")
async def mul(interaction: discord.Interaction, value1: str, value2: str):
    try:
        num1 = MathService.to_float(value1)
        num2 = MathService.to_float(value2)
    except ValueError:
        await interaction.response.send_message("Invalid input. Please provide valid numbers.")
        return

    from_larg = large_num()
    result = MathService.mul(num1, num2)
    toStr = from_larg.toStr(result)
    
    new_title = "Result from multiply value1 * value2"
    embed = discord.Embed(
        title=new_title,
        description=f"{value1} * {value2} = {result}",
        color=discord.Color.red()
    )
    embed.add_field(name="Result", value=result, inline=False)
    embed.add_field(name="To Short", value=toStr, inline=False)
    
    await interaction.response.send_message(embed=embed)

@NumberFormat.tree.command(name="log", description="log 2 values")
@app_commands.describe(value1="Number", value2="Number")
async def log(interaction: discord.Interaction, value1: str, value2: str):
    try:
        num1 = MathService.to_float(value1)
        num2 = MathService.to_float(value2)
    except ValueError:
        await interaction.response.send_message("Invalid input. Please provide valid numbers.")
        return

    from_larg = large_num()
    result = MathService.log(num1, num2)
    toStr = from_larg.toStr(result)
    
    new_title = f"Result from log(value1, value2)"
    embed = discord.Embed(
        title=new_title,
        description=f"log({num1}, {num2}) = {result}",
        color=discord.Color.red()
    )
    embed.add_field(name="Result", value=result, inline=False)
    embed.add_field(name="To Short", value=toStr, inline=False)
    
    await interaction.response.send_message(embed=embed)

@NumberFormat.tree.command(name="short", description="for Example 1000 to 1k")
@app_commands.describe(value1="Number")
async def short(interaction: discord.Interaction, value1: str):
    try:
        num1 = MathService.to_float(value1)
    except ValueError:
        await interaction.response.send_message("Invalid input. Please provide valid numbers.")
        return

    from_larg = large_num()
    toStr = from_larg.toStr(num1)
    
    new_title = f"Short"
    embed = discord.Embed(
        title=new_title,
        description=f"{toStr}",
        color=discord.Color.red()
        )
    embed.add_field(name="Original Value", value=num1, inline=False)

    await interaction.response.send_message(embed=embed)

    
@NumberFormat.tree.command(name="pow", description="Power of ex. 10^3")
@app_commands.describe(value1="Number", value2="Number")
async def short(interaction: discord.Interaction, value1: str, value2: str):
    try:
        num1 = MathService.to_float(value1)
        num2 = MathService.to_float(value2)
    except ValueError:
        await interaction.response.send_message("Invalid input. Please provide valid numbers.")
        return

    from_larg = large_num()
    result = MathService.pow(num1, num2)
    toStr = from_larg.toStr(result)
    
    new_title = f"Pow"
    embed = discord.Embed(
        title=new_title,
        description=f"{toStr}",
        color=discord.Color.red()
        )
    embed.add_field(name="Original Value", value=f"{num1}^{num2}={result}", inline=False)
    
    await interaction.response.send_message(embed=embed)

@NumberFormat.tree.command(name="help", description="To Help figure out where i put my dinner at")
async def help(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Help find the commands",
        description="must use `/` before using a command",
        color=discord.Color.orange()
    )
    embed.add_field(
        name="add",
        value="Add 2 Values",
        inline=True
    )
    embed.add_field(
        name="div",
        value="Div 2 values",
        inline=True
    )
    embed.add_field(
        name="log",
        value="log(value1, value2)",
        inline=True
    )
    embed.add_field(
        name="mul",
        value="Mul 2 values",
        inline=True
    )
    embed.add_field(
        name="short",
        value="short ex. 1000 to 1k",
        inline=True
    )
    embed.add_field(
        name="sub",
        value="Sub 2 values",
        inline=True
    )
    embed.add_field(
        name="pow",
        value="Pow value1^value2",
        inline=True
    )
    embed.add_field(
        name="dm_disable",
        value="Disables DM",
        inline=True
    )
    embed.add_field(
        name="dm_enable",
        value="Enables DM",
        inline=True
    )
    embed.add_field(
        name="dm",
        value="Dm's the person from the Server",
        inline=True
    )
    embed.add_field(
        name="post",
        value="Select from general, lua, bug_reports",
        inline=True
    )
    await interaction.response.send_message(embed=embed)

async def send_help(interaction: discord.Interaction):
    option = [
        discord.SelectOption(label="Question", value="general"),
        discord.SelectOption(label="Lua Code Help", value="lua"),
        discord.SelectOption(label="Bug Report", value="bug")
    ]
    select_menu = discord.ui.Select(
        placeholder='Select the type of help requested...',
        options=option,
        min_values=1,
        max_values=1
    )

    async def select_call(inter: discord.Interaction):
        select_type = select_menu.values[0]
        await inter.response.send_message(f"You have selected {select_type}", ephemeral=True)

        await inter.user.send(f"Please describe the help you need regarding {select_type}.")
        def check(message):
            return message.author == inter.user and isinstance(message.channel, discord.DMChannel)
        
        user_rep = await NumberFormat.wait_for('message', check=check)
        help_req = user_rep.content
        
        # Map types to channels
        channel_map = {
            "general": 1277823412072484894,
            "lua": 1279066096778870786,
            "bug": 1279082464538525800
        }
        channel_id = channel_map.get(select_type)
        channel = NumberFormat.get_channel(channel_id)

        if channel is None:
            await inter.user.send("The help channel does not exist.")
            return
        
        embed = discord.Embed(
            title="Help Requested",
            description=help_req,
            color=discord.Color.blue()
        )
        embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar.url)
        embed.add_field(name="Request Type", value=select_type.capitalize(), inline=False)
        
        # Retrieve and mention the role if the help type is 'lua'
        if select_type == "lua":
            role = interaction.guild.get_role(1279110158290780223)
            if role:
                await channel.send(content=f"{role.mention}", embed=embed)
            else:
                await channel.send(embed=embed)
                await inter.user.send("The specified role does not exist or cannot be mentioned.")
        else:
            await channel.send(embed=embed)
        
        await interaction.user.send("Your help request has been posted.")

    select_menu.callback = select_call
    view = discord.ui.View()
    view.add_item(select_menu)

    await interaction.response.send_message("Select the type of help request from the dropdown:", view=view, ephemeral=True)

@NumberFormat.tree.command(name="post", description="Able to create a post or just ask a general question")
async def post(interaction: discord.Interaction):
    try:
        await send_help(interaction)
    except discord.Forbidden:
        await interaction.response.send_message('I cannot send you a DM. Please ensure your DMs are open.', ephemeral=True)

@NumberFormat.tree.command(name="dm", description="Send a direct message to a member.")
@app_commands.describe(member="The member to DM", message="The message to send")
async def dm(interaction: discord.Interaction, member: discord.Member, message: str):
    global dm_command_enabled

    if not dm_command_enabled:
        await interaction.response.send_message('DMs are currently disabled.', ephemeral=True)
        return

    try:
        if member.dm_channel is None:
            await member.create_dm()

        local = datetime.now()
        formatted_time = local.strftime('%m/%d/%Y %I:%M:%S %p')

        embed = discord.Embed(
            title="Its Yeeeee Boi Slim Shady",
            description=message,
            color=discord.Color.blue()
        )
        embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar.url)
        embed.set_footer(text=f"Sent at {formatted_time}")

        await member.dm_channel.send(embed=embed)
        await interaction.response.send_message(f"Successfully sent a DM to {member.display_name}.", ephemeral=True)

    except discord.Forbidden:
        await interaction.response.send_message(f"Could not send DM to {member.display_name}. They might have DMs disabled.", ephemeral=True)
    except Exception as e:
        await interaction.response.send_message(f"An error occurred: {str(e)}", ephemeral=True)

@NumberFormat.tree.command(name="dm_disable", description="Disable the /dm command.")
async def dm_disable(interaction: discord.Interaction):
    global dm_command_enabled
    guild = interaction.guild
    role_disabled = discord.utils.get(guild.roles, name="DM_Disabled")
    role_enabled = discord.utils.get(guild.roles, name="DM_Enable")
    if role_enabled:
        await interaction.user.remove_roles(role_enabled)
    if role_disabled:
        await interaction.user.add_roles(role_disabled)
    dm_command_enabled = False

    await interaction.response.send_message('The /dm command has been disabled.')

@NumberFormat.tree.command(name="dm_enable", description="Enable the /dm command.")
async def dm_enable(interaction: discord.Interaction):
    global dm_command_enabled
    guild = interaction.guild

    role_enabled = discord.utils.get(guild.roles, name="DM_Enable")
    role_disabled = discord.utils.get(guild.roles, name="DM_Disabled")
    if role_disabled:
        try:
            await interaction.user.remove_roles(role_disabled)
        except discord.Forbidden:
            await interaction.response.send_message('I do not have permission to remove the "DM_Disabled" role.', ephemeral=True)
            return

    if role_enabled:
        try:
            await interaction.user.add_roles(role_enabled)
        except discord.Forbidden:
            await interaction.response.send_message('I do not have permission to add the "DM_Enabled" role.', ephemeral=True)
            return

    dm_command_enabled = True

    await interaction.response.send_message('The /dm command has been enabled.')

NumberFormat.run('Your Bot Token')